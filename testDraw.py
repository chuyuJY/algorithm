import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams["font.family"] = "SimHei"      # 中文显示

def drawBase(circle, x, y):
    # 1.画圆
    circle = circle
    for r in circle:
        # 圆心，半径，。。。
        fig = plt.Circle((r, 0), 5, color='y', fill=False, linestyle='--')
        plt.gcf().gca().add_artist(fig)
    # 等比例，否则不圆
    plt.axis('equal')

    # 2.船的位置
    x = x
    y = y
    # 第一种输出方式
    # xpoint = np.array(x)
    # ypoint = np.array(y)
    # plt.plot(xpoint, ypoint, '.')
    # 第二种输出方式
    plt.scatter(x, y, label='Ship', marker='.')

    # 3.基站位置
    x = circle
    y = [0] * len(circle)
    plt.scatter(x, y, label='Base Station', marker='o')

    # 4.坐标系
    plt.xlim(0, 25)
    plt.ylim(-10, 10)
    plt.xlabel("X")
    plt.ylabel("Y")
    # 设置水平参考线
    plt.axhline(y=0, color='green', linestyle='-', linewidth=1.5)
    # 显示标签
    plt.legend()
    # 保存图片
    plt.savefig('test.png')
    # 显示图
    plt.show()


if __name__ == '__main__':
    circle = [3, 12, 15]
    x = [1, 2, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15]
    y = [1, 3, 4, 5, 4, 3, 3, 2, 4, 2, 3, 4, 5]
    # circle = [6]
    # x = [3, 4]
    # y = [4, 2]
    drawBase(circle, x, y)

