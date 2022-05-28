from typing import List
import matplotlib.pyplot as plt
import numpy as np
import math

def drawPlaneStatus(coords: List[List[int]], r: int):
    x = np.array([i[0] for i in coords])
    y = np.array([i[1] for i in coords])
    # 设置坐标轴名称
    plt.xlabel("x")
    plt.ylabel("y")
    # 设置大小
    size = 5
    # 设置颜色
    colors = np.array(["green"])
    plt.scatter(x, y, s=size, c=colors)
    # 画圆
    for coord in coords:
        fig = plt.Circle((coord[0], coord[1]), r, color='y', fill=False, linestyle="--")
        plt.gcf().gca().add_artist(fig)
    plt.axis('equal')

    # 设置参考线
    # 水平
    # plt.axhline(y=6745367, color='green', linestyle='-', linewidth=1.5)
    # 垂直
    # temp = sorted(coords, key=lambda x: x[0])
    # print(temp)
    # x = temp[int(len(temp)/2)][0]
    # plt.axvline(x=x, color='red', linestyle='-', linewidth=1)

    # 网格线
    plt.grid(ls='--')
    plt.show()

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    coords = [[11806255, 6744952], [11806637, 6745243], [11806180, 6745237],
              [11806250, 6745224], [11806017, 6745332], [11806750, 6745454],
              [11807214, 6745367], [11805879, 6745067], [11806752, 6745063],
              [11806519, 6745541], [11806494, 6745085], [11806668, 6744803],
              [11806204, 6745504]]
    r = 100
    drawPlaneStatus(coords, r)

    # pA = P(11806017, 6745332)
    # pB = P(11806180, 6745237)
    # print(int(round(math.sqrt((pA.x - pB.x) * (pA.x - pB.x) + (pA.y - pB.y) * (pA.y - pB.y)))))