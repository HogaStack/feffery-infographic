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
    ...others
}) => {

    const containerRef = useRef(null);

    useEffect(() => {
        const infographic = new InfographicCore({
            container: containerRef.current,
            width: '100%',
            height: '100%',
        });

        infographic.render(syntax);

        return () => {
            infographic.destroy();
        };
    }, [syntax]);

    return (
        <div
            id={id}
            style={style}
            className={className}
            ref={containerRef}
        />
    );
}

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
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default Infographic;
