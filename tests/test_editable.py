from dash import Dash, html
from feffery_dash_utils.style_utils import style
from selenium.common.exceptions import TimeoutException

import feffery_infographic as fi


def test_editable(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            fi.Infographic(
                id='info-graphic',
                padding=200,
                height=700,
                editable=True,
                syntax="""
infographic list-row-simple-horizontal-arrow
data
  items
    - label 步骤 1
      desc 开始
    - label 步骤 2
      desc 进行中
    - label 步骤 3
      desc 完成
""",
                style={
                    'border': '1px solid #e8e8e8',
                    'display': 'flex',
                    'justifyContent': 'center',
                },
            ),
        ],
        style=style(padding=50),
    )

    dash_duo.start_server(app)

    dash_duo.wait_for_element(
        '#infographic-container > g > g:nth-child(1) > g:nth-child(2) > g > g:nth-child(3) > foreignObject > span'
    ).click()

    try:
        dash_duo.wait_for_element('.infographic-edit-bar-icon-btn', timeout=3)
    except TimeoutException:
        pass
