<p align="center">
	<img src="./imgs/fi-logo.svg" height=300></img>
</p>
<h1 align="center">feffery-infographic</h1>
<div align="center">

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/HogaStack/feffery-infographic/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-infographic.svg?color=dark-green)](https://pypi.org/project/feffery-infographic)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/HogaStack/feffery-infographic.svg)](http://isitmaintained.com/project/HogaStack/feffery-infographic 'Average time to resolve an issue')
[![Percentage of issues still open](http://isitmaintained.com/badge/open/HogaStack/feffery-infographic.svg)](http://isitmaintained.com/project/HogaStack/feffery-infographic 'Percentage of issues still open')

</div>

[简体中文](./README.md) | English

A component library for the `Python` full-stack application development framework [Plotly Dash](https://github.com/plotly/dash), based on [AntV Infographic](https://github.com/antvis/infographic), providing rich **infographic rendering** capabilities.

## 1 Installation

```bash
pip install feffery-infographic
```

## 2 API

### Infographic Component

| Property Name           | Type                 | Default | Description                                                                                                                                      |
| :---------------------- | :------------------- | :------ | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| id                      | `string`             | -       | Unique ID for the component.                                                                                                                     |
| key                     | `string`             | -       | Update the `key` value of the current component to force a redraw.                                                                               |
| style                   | `dict`               | -       | CSS style object for the current component.                                                                                                      |
| className               | `string`             | -       | CSS class name for the current component.                                                                                                        |
| syntax                  | `string`             | -       | **Required**, syntax string for defining the infographic content.                                                                                |
| width                   | `number` \| `string` | -       | Width of the infographic container, supports number or string (e.g., `'100%'`).                                                                  |
| height                  | `number` \| `string` | -       | Height of the infographic container, supports number or string (e.g., `'500px'`).                                                                |
| padding                 | `number` \| `list`   | -       | Padding of the infographic container, supports number or array format (e.g., `[top, right, bottom, left]`).                                      |
| exportTrigger           | `dict`               | -       | Configuration object for triggering image export or download operations. Each update triggers the operation and resets to empty after execution. |
| exportEvent             | `dict`               | -       | Data object listening for the latest image export event.                                                                                         |
| debugWindowInstanceName | `string`             | -       | For debugging purposes. If set, mounts the current component instance to the `window` object under the specified variable name.                  |

**`exportTrigger` Configuration Details:**

- `type`: _string_, format of the exported image. Options are `'png'`, `'svg'`. Default is `'png'`.
- `dpr`: _number_, pixel ratio when exporting `'png'` images. Default is `1`.
- `download`: _boolean_, whether to automatically trigger browser download. Default is `True`.
- `fileName`: _string_, name of the downloaded file (without extension). Default is `'infographic_export'`.

**`exportEvent` Structure Details:**

- `timestamp`: _number_, timestamp when the event was triggered.
- `type`: _string_, format of the exported image. Possible values are `'png'` or `'svg'`.
- `data`: _string_, `dataURL` data of the exported image.

## 3 Basic Usage

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
            # Define infographic syntax
            syntax="""
infographic list-row-simple-horizontal-arrow
data
  items
    - label Step 1
      desc Start
    - label Step 2
      desc In Progress
    - label Step 3
      desc Completed
"""
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
```

## 4 Infographic Syntax Reference

👉 https://infographic.antv.vision/learn/infographic-syntax

## 5 All Available Infographic Examples

👉 https://infographic.antv.vision/gallery

## 6 Contributors

<a href = "https://github.com/HogaStack/feffery-infographic/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=HogaStack/feffery-infographic"/>
</a>
