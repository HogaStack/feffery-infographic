import json
import time

from dash import Dash, html, set_props
from dash.dependencies import Input, Output
from feffery_dash_utils.style_utils import style

import feffery_infographic as fi


def test_export_image(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            html.Button('generate image data', id='generate-image-data'),
            fi.Infographic(
                id='info-graphic',
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
            html.Pre(id='exported-image-data'),
        ],
        style=style(padding=50),
    )

    @app.callback(Input('generate-image-data', 'n_clicks'))
    def generate_image_data(n_clicks):
        if n_clicks == 1:
            set_props('info-graphic', {'exportTrigger': {'dpr': 2}})
        elif n_clicks == 2:
            set_props('info-graphic', {'exportTrigger': {'type': 'svg'}})

    app.clientside_callback(
        """(exportEvent) => {
            return JSON.stringify(exportEvent)
        }""",
        Output('exported-image-data', 'children'),
        Input('info-graphic', 'exportEvent'),
        prevent_initial_call=True,
    )

    dash_duo.start_server(app)

    dash_duo.wait_for_element('#generate-image-data').click()

    time.sleep(0.5)

    exported_image_data = json.loads(dash_duo.find_element('#exported-image-data').text)

    assert exported_image_data.get('data', '').startswith('data:image/png;base64'), (
        '应该有合法png图片数据输出结果'
    )

    dash_duo.wait_for_element('#generate-image-data').click()

    time.sleep(0.5)

    exported_image_data = json.loads(dash_duo.find_element('#exported-image-data').text)

    assert exported_image_data.get('data', '').startswith('data:image/svg'), (
        '应该有合法svg图片数据输出结果'
    )
