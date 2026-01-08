// react核心
import { useEffect, useRef } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { Infographic as InfographicCore } from '@antv/infographic';
// 工具函数
import { exportInfographic } from '../utils';

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
    exportTrigger,
    debugWindowInstanceName,
    setProps,
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
        if (infographicRef.current && exportTrigger) {
            // 处理信息图导出及下载
            exportInfographic(
                infographicRef.current,
                {
                    type: 'png',
                    dpr: 1,
                    fileName: 'infographic_export',
                    download: true,
                    ...exportTrigger,
                },
                setProps
            );
            // 重置exportTrigger
            setProps({ exportTrigger: null });
        }
    }, [exportTrigger]);

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

        if (debugWindowInstanceName) {
            window[debugWindowInstanceName] = infographicRef.current;
        }

        return () => {
            infographicRef.current.destroy();
            if (debugWindowInstanceName) {
                delete window[debugWindowInstanceName];
            }
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
     * 每次有效更新都会触发针对当前信息图的图片导出、下载操作，每次执行后都会被重置为空值
     * (Each time a valid update is triggered, a picture export and download operation will be triggered for the current infographic, and each time it will be reset to an empty value)
     */
    exportTrigger: PropTypes.shape({
        /**
         * 图片导出类型，可选项有`'png'`、`'svg'`
         * (Image export type, optional items include `'png'` and `'svg'`)
         * 默认值：`'png'`
         * (Default: `'png'`)
         */
        type: PropTypes.oneOf(['png', 'svg']),
        /**
         * 当导出`'png'`类型图片时，用于设置导出图片的像素比
         * (When exporting the `'png'` type image, set the export image pixel ratio)
         * 默认值：`1`
         * (Default: `1`)
         */
        dpr: PropTypes.number,
        /**
         * 是否触发下载操作
         * (Whether to trigger the download operation)
         * 默认值：`true`
         * (Default: `true`)
         */
        download: PropTypes.bool,
        /**
         * 当触发下载操作时，控制下载文件的文件名
         * (When triggering the download operation, control the download file name)
         * 默认值：`'infographic_export'`
         * (Default: `'infographic_export'`)
         */
        fileName: PropTypes.string,
    }),

    /**
     * 记录最近一次通过参数`exportTrigger`有效触发的图片导出操作事件信息
     * (Record the latest event information of the image export operation triggered by the parameter `exportTrigger`)
     */
    exportEvent: PropTypes.shape({
        /**
         * 事件时间戳
         */
        timestamp: PropTypes.number,
        /**
         * 图片类型，可能值有`'png'`、`'svg'`
         */
        type: PropTypes.oneOf(['png', 'svg']),
        /**
         * 图片对应`dataURL`数据
         */
        data: PropTypes.string,
    }),

    /**
     * 调试用参数，有效设置后会将当前信息图实例挂载到`window`对象下对应的变量名上
     * (Debugging parameters, valid setting will mount the current infographic instance to the `window` object under the corresponding variable name)
     */
    debugWindowInstanceName: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default Infographic;
