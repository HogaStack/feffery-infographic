import json  # noqa: I001
import time
import uuid
import dash
from dash import html
from flask import Response
import feffery_infographic as fi
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, State
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

full_syntax = """
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


@app.server.route('/sse-syntax-example')
def stream():
    def _stream():
        pieces = []
        for i in range(0, len(full_syntax), 30):
            pieces.append(full_syntax[i : i + 30])

        for p in pieces:
            time.sleep(0.2)
            yield 'data: {}\n\n'.format(
                json.dumps(
                    {'syntax': p.replace('\n', '<换行>'), 'key': str(uuid.uuid4())},
                    ensure_ascii=False,
                )
            )

    return Response(_stream(), mimetype='text/event-stream')


app.layout = lambda: html.Div(
    [
        fuc.FefferyEventSource(id='syntax-sse', url='/sse-syntax-example'),
        fac.AntdCenter(fi.Infographic(id='info-graphic', syntax='', padding=25, height=800)),
    ],
    style=style(padding=50),
)

app.clientside_callback(
    """
(data, originSyntax) => {
    if ( data ) {
        data = JSON.parse(data);
        dash_clientside.set_props('info-graphic', { syntax: originSyntax + data.syntax.replaceAll('<换行>', '\\n') });
    }
}
""",
    Input('syntax-sse', 'data'),
    State('info-graphic', 'syntax'),
)

if __name__ == '__main__':
    app.run(debug=True)
