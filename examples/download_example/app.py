import dash  # noqa: I001
from dash import html
import feffery_infographic as fi
import feffery_antd_components as fac
from dash.dependencies import Input, Output
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

syntax_demo = """
infographic sequence-ascending-stairs-3d-simple
data
  title 企业优势列表
  desc 展示企业在不同维度上的核心优势与表现值
  items
    - label 品牌影响力
      value 85
      desc 在目标用户群中具备较强认知与信任度
      time 2021
      icon mingcute/diamond-2-fill
      illus creative-experiment
    - label 技术研发力
      value 90
      desc 拥有自研核心系统与持续创新能力
      time 2022
      icon mingcute/code-fill
      illus code-thinking
    - label 市场增长快
      value 78
      desc 近一年用户规模实现快速增长
      time 2023
      icon mingcute/wallet-4-line
      illus business-analytics
    - label 服务满意度
      value 88
      desc 用户对服务体系整体评分较高
      time 2020
      icon mingcute/happy-line
      illus feeling-happy
    - label 数据资产全
      value 92
      desc 构建了完整用户标签与画像体系
      time 2022
      icon mingcute/user-4-line
      illus mobile-photos
    - label 创新能力强
      value 83
      desc 新产品上线频率高于行业平均
      time 2023
      icon mingcute/rocket-line
      illus creativity
theme light
  palette antv
"""


app.layout = lambda: html.Div(
    [
        fac.AntdSpace(
            [
                fac.AntdButton('导出svg', id='export-svg'),
                fac.AntdButton('导出png', id='export-png'),
            ],
            size='small',
        ),
        fac.AntdCenter(
            fi.Infographic(id='info-graphic', syntax=syntax_demo, padding=25, height=800)
        ),
    ],
    style=style(padding=50),
)


@app.callback(
    Output('info-graphic', 'exportTrigger'),
    [Input('export-svg', 'nClicks'), Input('export-png', 'nClicks')],
    prevent_initial_call=True,
)
def export_image(*args):
    if dash.ctx.triggered_id == 'export-svg':
        return {'type': 'svg'}
    elif dash.ctx.triggered_id == 'export-png':
        return {'type': 'png'}


if __name__ == '__main__':
    app.run(debug=True)
