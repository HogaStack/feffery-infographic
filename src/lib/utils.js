/**
 * 处理信息图的导出及下载
 */
async function exportInfographic(instance, triggerOptions, setProps) {
    const dataURL = await instance.toDataURL({
        type: triggerOptions.type,
        dpr: triggerOptions.dpr,
    });

    // 处理下载过程
    if (triggerOptions.download) {
        const response = await fetch(dataURL);
        const blob = await response.blob();
        const blobUrl = URL.createObjectURL(blob);

        const link = document.createElement('a');
        link.style.display = 'none';
        link.href = blobUrl;
        link.download = `${triggerOptions.fileName}.${triggerOptions.type}`;

        document.body.appendChild(link);
        link.click();

        setTimeout(() => {
            document.body.removeChild(link);
            URL.revokeObjectURL(blobUrl);
        }, 100);
    }
    setProps({
        exportEvent: {
            timestamp: Date.now(),
            type: triggerOptions.type || 'png',
            data: dataURL,
        },
    });
}

export { exportInfographic };
