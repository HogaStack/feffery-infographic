# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class Infographic(Component):
    """An Infographic component.
信息图渲染组件
(Infographic render component)

Keyword arguments:

- id (string; optional):
    组件唯一id  (The unique id of this component).

- className (string; optional):
    当前组件css类  (The css class of the current component).

- height (number | string; optional):
    信息图高度，支持数值型和字符型输入  (Infographic height, support numeric and
    character input).

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果  （Force update the `key` value of
    the current component, which can force a redraw of the current
    component）.

- padding (number | list of numbers; optional):
    信息图像素内边距，支持数值型，或格式如`[上, 右, 下, 左]`各自方向上像素内边距的数组  (Infographic pixel
    margin, support numeric, or format like `[top, right, bottom,
    left]` array of each direction pixel margin).

- syntax (string; required):
    必填，信息图语法  (Required, infographic syntax).

- width (number | string; optional):
    信息图宽度，支持数值型和字符型输入  (Infographic width, support numeric and
    character input)."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'feffery_infographic'
    _type = 'Infographic'


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
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'height', 'key', 'padding', 'style', 'syntax', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'height', 'key', 'padding', 'style', 'syntax', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['syntax']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Infographic, self).__init__(**args)

setattr(Infographic, "__init__", _explicitize_args(Infographic.__init__))
