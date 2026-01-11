<p align="center">
	<img src="./imgs/fi-logo.svg" height=300></img>
</p>
<h1 align="center">feffery-infographic</h1>
<div align="center">

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/HogaStack/feffery-infographic/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-infographic.svg?color=dark-green)](https://pypi.org/project/feffery-infographic)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/HogaStack/feffery-infographic.svg)](http://isitmaintained.com/project/HogaStack/feffery-infographic "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/HogaStack/feffery-infographic.svg)](http://isitmaintained.com/project/HogaStack/feffery-infographic "Percentage of issues still open")

</div>

适用于`Python`全栈应用开发框架[Plotly Dash](https://github.com/plotly/dash)的组件库，基于[AntV Infographic](https://github.com/antvis/infographic)，提供丰富的**信息图渲染**功能。

## 1 安装

```bash
pip install feffery-infographic
```

## 2 API

### Infographic 信息图渲染组件

| 属性名 | 类型 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- |
| id | `string` | - | 组件唯一 id |
| key | `string` | - | 对当前组件的 `key` 值进行更新，可实现强制重绘当前组件的效果 |
| style | `dict` | - | 当前组件 css 样式 |
| className | `string` | - | 当前组件 css 类名 |
| syntax | `string` | - | **必填**，信息图语法 |
| width | `number` \| `string` | - | 信息图宽度，支持数值型和字符型输入 |
| height | `number` \| `string` | - | 信息图高度，支持数值型和字符型输入 |
| padding | `number` \| `list` | - | 信息图像素内边距，支持数值型，或格式如 `[上, 右, 下, 左]` 各自方向上像素内边距的数组 |
| exportTrigger | `dict` | - | 每次有效更新都会触发针对当前信息图的图片导出、下载操作，每次执行后都会被重置为空值，包含 `type`、`dpr`、`download`、`fileName` 键 |
| exportEvent | `dict` | - | 记录最近一次通过参数 `exportTrigger` 有效触发的图片导出操作事件信息，包含 `timestamp`、`type`、`data` 键 |
| debugWindowInstanceName | `string` | - | 调试用参数，有效设置后会将当前信息图实例挂载到 `window` 对象下对应的变量名上 |

**exportTrigger 配置项：**

- `type`: *string*，图片导出类型，可选项有 `'png'`、`'svg'`，默认为 `'png'`
- `dpr`: *number*，当导出 `'png'` 类型图片时，用于设置导出图片的像素比，默认为 `1`
- `download`: *boolean*，是否触发下载操作，默认为 `True`
- `fileName`: *string*，当触发下载操作时，控制下载文件的文件名，默认为 `'infographic_export'`

**exportEvent 结构：**

- `timestamp`: *number*，事件时间戳
- `type`: *string*，图片类型，可能值有 `'png'`、`'svg'`
- `data`: *string*，图片对应 `dataURL` 数据

## 3 基本使用

```python
import dash
from dash import html
import feffery_infographic as fi

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fi.Infographic(
            padding=20,
            height=500,
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
"""
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
```

## 4 信息图语法参考

👉 https://infographic.antv.vision/learn/infographic-syntax

## 5 全部可用信息图示例

👉 https://infographic.antv.vision/gallery

## 6 贡献者

<a href = "https://github.com/HogaStack/feffery-infographic/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=HogaStack/feffery-infographic"/>
</a>

## 7 更多应用开发教程

> 微信公众号「玩转 Dash」，欢迎扫码关注 👇

<p align="center" >
  <img src="./imgs/公众号.png" height=220 />
</p>

> 「玩转 Dash」知识星球，海量教程案例模板资源，专业的答疑咨询服务，欢迎扫码加入 👇

<p align="center" >
  <img src="./imgs/知识星球.jpg" height=220 />
</p>
