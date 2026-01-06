import time

from dash import Dash, html, set_props
from dash.dependencies import Input
from feffery_dash_utils.style_utils import style

import feffery_infographic as fi


def test_basic_props_update(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            html.Button('change height', id='change-info-graphic-height'),
            fi.Infographic(
                id='info-graphic',
                padding=200,
                height=700,
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

    @app.callback(
        Input('change-info-graphic-height', 'n_clicks'),
    )
    def change_infographic_height(n_clicks):
        set_props(
            'info-graphic',
            {'height': 400},
        )

    dash_duo.start_server(app)

    dash_duo.wait_for_element('#change-info-graphic-height').click()

    time.sleep(0.5)

    assert dash_duo.find_element('#info-graphic').value_of_css_property('height') == '400px', (
        '图表高度应该更新为400px'
    )
