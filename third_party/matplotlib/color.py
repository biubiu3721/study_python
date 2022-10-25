import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
# define some random data that emulates your indeed code:
NCURVES = 100
values = range(NCURVES)
data = np.arange(30)

datas = [ data + i for i in range(NCURVES)]  # 需要绘制的曲线

fig = plt.figure() # set a fig instance
ax = fig.add_subplot(111) # set subplot as 111

if 1:
    cm = plt.get_cmap('nipy_spectral')
    # 设置离散 value 的取值范围 0 to 99
    cNorm = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)

lines = []
for idx in range(NCURVES):
    print('values[idx]', values[idx])

    colorVal = scalarMap.to_rgba(values[idx]) # 根据 value 提取颜色
    print("colorVal", colorVal)
    colorText = ( 'color: (%4.2f,%4.2f,%4.2f)'%(colorVal[0],colorVal[1],colorVal[2]) )
    retLine = ax.plot(datas[idx], color=colorVal, label=colorText)
    lines.append(retLine)
print(lines)
#added this to get the legend to work
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')
ax.grid()
plt.show()