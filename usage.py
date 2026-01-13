import dash  # noqa: I001
from dash import html
import feffery_infographic as fi

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fi.Infographic(
            # 定义信息图语法
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
        )
    ],
    style={'padding': 50},
)

if __name__ == '__main__':
    app.run(debug=True)
