import time

from dash import Dash, html, set_props
from dash.dependencies import Input
from feffery_dash_utils.style_utils import style

import feffery_infographic as fi


def test_syntax_stream_update(dash_duo):
    app = Dash(__name__)
    app.layout = html.Div(
        [
            html.Button('simulate stream syntax', id='simulate-stream-syntax'),
            fi.Infographic(
                id='info-graphic',
                padding=200,
                height=700,
                syntax='',
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
        Input('simulate-stream-syntax', 'n_clicks'),
    )
    def simulate_stream_syntax(n_clicks):
        if n_clicks == 1:
            set_props(
                'info-graphic',
                {
                    'syntax': """
infographic chart-bar-plain-text
data
  title 年度营收增长
  desc 展示近三年及本年目标营收对比（单位：亿元）
  items
    - label 2021年
      value 120
      desc 转型初期，稳步试水
      icon lucide/sprout
theme light
  palette antv
"""
                },
            )

        elif n_clicks == 2:
            set_props(
                'info-graphic',
                {
                    'syntax': """
infographic chart-bar-plain-text
data
  title 年度营收增长
  desc 展示近三年及本年目标营收对比（单位：亿元）
  items
    - label 2021年
      value 120
      desc 转型初期，稳步试水
      icon lucide/sprout
    - label 2022年
      value 150
      desc 平台优化，效率显著提升
      icon lucide/zap
theme light
  palette antv
"""
                },
            )

        elif n_clicks == 3:
            set_props(
                'info-graphic',
                {
                    'syntax': """
infographic chart-bar-plain-text
data
  title 年度营收增长
  desc 展示近三年及本年目标营收对比（单位：亿元）
  items
    - label 2021年
      value 120
      desc 转型初期，稳步试水
      icon lucide/sprout
    - label 2022年
      value 150
      desc 平台优化，效率显著提升
      icon lucide/zap
    - label 2023年
      value 190
      desc 深化数智融合，全面增长
      icon lucide/brain-circuit
theme light
  palette antv
"""
                },
            )

        elif n_clicks == 4:
            set_props(
                'info-graphic',
                {
                    'syntax': """
infographic chart-bar-plain-text
data
  title 年度营收增长
  desc 展示近三年及本年目标营收对比（单位：亿元）
  items
    - label 2021年
      value 120
      desc 转型初期，稳步试水
      icon lucide/sprout
    - label 2022年
      value 150
      desc 平台优化，效率显著提升
      icon lucide/zap
    - label 2023年
      value 190
      desc 深化数智融合，全面增长
      icon lucide/brain-circuit
    - label 2024年
      value 240
      desc 拓展生态协同，冲击新高
      icon lucide/trophy
theme light
  palette antv
"""
                },
            )

    dash_duo.start_server(app)

    dash_duo.wait_for_element('#simulate-stream-syntax')

    for i in range(4):
        dash_duo.find_element('#simulate-stream-syntax').click()

        time.sleep(0.5)

        assert (
            dash_duo.find_element(
                f'#infographic-container > g:nth-child(2) > g:nth-child(6) > g:nth-child({1 + i}) > foreignObject > span'
            ).text
            == f'{2021 + i}年'
        ), f'当前元素内容应该为 {2021 + i}年'
