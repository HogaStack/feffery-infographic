import dash
from dash import html, set_props
import feffery_infographic as fi
from dash.dependencies import Input
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__, compress=True)

app.layout = html.Div(
    [
        html.Button("change infographic", id="change-info-graphic"),
        fi.Infographic(
            id="info-graphic",
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
        ),
    ],
    style=style(padding=50),
)


@app.callback(
    Input("change-info-graphic", "n_clicks"),
)
def change_infographic(n_clicks):
    set_props(
        "info-graphic",
        {
            "syntax": """
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
    set_props("change-info-graphic", {"disabled": True})


if __name__ == "__main__":
    app.run(debug=True)
