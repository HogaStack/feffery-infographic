import time

from dash import Dash, html
from feffery_dash_utils.style_utils import style
from selenium.common.exceptions import NoSuchElementException

import feffery_infographic as fi


def test_debug_instance_name(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            fi.Infographic(
                id='info-graphic',
                debugWindowInstanceName='demoInforaphic',
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
                    'display': 'flex',
                    'justifyContent': 'center',
                },
            ),
        ],
        style=style(padding=50),
    )

    dash_duo.start_server(app)

    dash_duo.wait_for_element('#info-graphic')

    # 模拟js销毁信息图元素
    dash_duo.driver.execute_script('window.demoInforaphic.destroy();')

    time.sleep(0.5)

    # 尝试定位信息图内容
    infographic_destroyed = False
    try:
        dash_duo.find_element('#infographic-container > g')
    except NoSuchElementException:
        infographic_destroyed = True

    assert infographic_destroyed, '信息图应该已被销毁'
