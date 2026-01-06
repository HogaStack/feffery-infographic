// react核心
import { useEffect, useRef } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { Infographic as InfographicCore } from '@antv/infographic';

/**
 * 信息图渲染组件
 * (Infographic render component)
 */
const Infographic = ({
    id,
    style,
    className,
    syntax,
    width,
    height,
    padding,
    ..._others
}) => {
    const infographicRef = useRef(null);
    const containerRef = useRef(null);

    useEffect(() => {
        if (infographicRef.current) {
            infographicRef.current.update({
                width: width,
                height: height,
                padding: padding,
            });
        }
    }, [width, height, padding]);

    useEffect(() => {
        if (infographicRef.current) {
            infographicRef.current.render(syntax);
        }
    }, [syntax]);

    useEffect(() => {
        infographicRef.current = new InfographicCore({
            container: containerRef.current,
            width: width,
            height: height,
            padding: padding,
        });

        if (syntax) {
            infographicRef.current.render(syntax);
        }

        return () => {
            infographicRef.current.destroy();
        };
    }, []);

    return (
        <div id={id} style={style} className={className} ref={containerRef} />
    );
};

Infographic.propTypes = {
    /**
     * 组件唯一id
     * (The unique id of this component)
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     * （Force update the `key` value of the current component, which can force a redraw of the current component）
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式字典，键名请使用小驼峰命名法
     * (The style dictionary of the current component, the key name please use camelCase naming)
     */
    style: PropTypes.object,

    /**
     * 当前组件css类
     * (The css class of the current component)
     */
    className: PropTypes.string,

    /**
     * 必填，信息图语法
     * (Required, infographic syntax)
     */
    syntax: PropTypes.string.isRequired,

    /**
     * 信息图宽度，支持数值型和字符型输入
     * (Infographic width, support numeric and character input)
     */
    width: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),

    /**
     * 信息图高度，支持数值型和字符型输入
     * (Infographic height, support numeric and character input)
     */
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),

    /**
     * 信息图像素内边距，支持数值型，或格式如`[上, 右, 下, 左]`各自方向上像素内边距的数组
     * (Infographic pixel margin, support numeric, or format like `[top, right, bottom, left]` array of each direction pixel margin)
     */
    padding: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number),
    ]),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default Infographic;
