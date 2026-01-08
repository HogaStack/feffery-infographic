# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401

from dash.development.base_component import Component, _explicitize_args
from typing_extensions import Literal, NotRequired, TypedDict  # noqa: F401

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex]


class Infographic(Component):
    """An Infographic component.
    信息图渲染组件
    (Infographic render component)

    Keyword arguments:

    - id (string; optional):
        组件唯一id (The unique id of this component).

    - key (string; optional):
        对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果 （Force update the `key` value of
        the current component, which can force a redraw of the current
        component）.

    - className (string; optional):
        当前组件css类 (The css class of the current component).

    - syntax (string; required):
        必填，信息图语法 (Required, infographic syntax).

    - width (number | string; optional):
        信息图宽度，支持数值型和字符型输入 (Infographic width, support numeric and
        character input).

    - height (number | string; optional):
        信息图高度，支持数值型和字符型输入 (Infographic height, support numeric and
        character input).

    - padding (number | list of numbers; optional):
        信息图像素内边距，支持数值型，或格式如`[上, 右, 下, 左]`各自方向上像素内边距的数组 (Infographic pixel
        margin, support numeric, or format like `[top, right, bottom,
        left]` array of each direction pixel margin).

    - exportTrigger (dict; optional):
        每次有效更新都会触发针对当前信息图的图片导出、下载操作，每次执行后都会被重置为空值 (Each time a valid
        update is triggered, a picture export and download operation will
        be triggered for the current infographic, and each time it will be
        reset to an empty value).

        `exportTrigger` is a dict with keys:

        - type (a value equal to: 'png', 'svg'; optional):
            图片导出类型，可选项有`'png'`、`'svg'` (Image export type, optional items
            include `'png'` and `'svg'`) 默认值：`'png'` (Default: `'png'`).

        - dpr (number; optional):
            当导出`'png'`类型图片时，用于设置导出图片的像素比 (When exporting the `'png'` type
            image, set the export image pixel ratio) 默认值：`1` (Default:
            `1`).

        - download (boolean; optional):
            是否触发下载操作 (Whether to trigger the download operation)
            默认值：`True` (Default: `True`).

        - fileName (string; optional):
            当触发下载操作时，控制下载文件的文件名 (When triggering the download operation,
            control the download file name) 默认值：`'infographic_export'`
            (Default: `'infographic_export'`).

    - exportEvent (dict; optional):
        记录最近一次通过参数`exportTrigger`有效触发的图片导出操作事件信息 (Record the latest event
        information of the image export operation triggered by the
        parameter `exportTrigger`).

        `exportEvent` is a dict with keys:

        - timestamp (number; optional):
            事件时间戳.

        - type (a value equal to: 'png', 'svg'; optional):
            图片类型，可能值有`'png'`、`'svg'`.

        - data (string; optional):
            图片对应`dataURL`数据.

    - debugWindowInstanceName (string; optional):
        调试用参数，有效设置后会将当前信息图实例挂载到`window`对象下对应的变量名上 (Debugging parameters,
        valid setting will mount the current infographic instance to the
        `window` object under the corresponding variable name)."""

    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_infographic'
    _type = 'Infographic'
    ExportTrigger = TypedDict(
        'ExportTrigger',
        {
            'type': NotRequired[Literal['png', 'svg']],
            'dpr': NotRequired[NumberType],
            'download': NotRequired[bool],
            'fileName': NotRequired[str],
        },
    )

    ExportEvent = TypedDict(
        'ExportEvent',
        {
            'timestamp': NotRequired[NumberType],
            'type': NotRequired[Literal['png', 'svg']],
            'data': NotRequired[str],
        },
    )

    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        syntax: typing.Optional[str] = None,
        width: typing.Optional[typing.Union[NumberType, str]] = None,
        height: typing.Optional[typing.Union[NumberType, str]] = None,
        padding: typing.Optional[typing.Union[NumberType, typing.Sequence[NumberType]]] = None,
        exportTrigger: typing.Optional['ExportTrigger'] = None,
        exportEvent: typing.Optional['ExportEvent'] = None,
        debugWindowInstanceName: typing.Optional[str] = None,
        **kwargs,
    ):
        self._prop_names = [
            'id',
            'key',
            'style',
            'className',
            'syntax',
            'width',
            'height',
            'padding',
            'exportTrigger',
            'exportEvent',
            'debugWindowInstanceName',
        ]
        self._valid_wildcard_attributes = []
        self.available_properties = [
            'id',
            'key',
            'style',
            'className',
            'syntax',
            'width',
            'height',
            'padding',
            'exportTrigger',
            'exportEvent',
            'debugWindowInstanceName',
        ]
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['syntax']:
            if k not in args:
                raise TypeError('Required argument `' + k + '` was not specified.')

        super(Infographic, self).__init__(**args)


setattr(Infographic, '__init__', _explicitize_args(Infographic.__init__))
