import math
import random
from typing import List
import pandas as pd

# 方位
direct = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]


# 飞机数据
class Planes:
    def __init__(self, planeId=None, x=None, y=None):
        self.planeId = planeId
        self.x = x
        self.y = y


class AlgorithmHW3:
    def __init__(self):
        reader = pd.read_csv('problem3_data.csv', usecols=['ID', 'lat', 'lon'])
        planesId = reader['ID'].values.tolist()
        planesLat = reader['lat'].values.tolist()
        planesLon = reader['lon'].values.tolist()
        # 存储飞机信息: id, x, y
        self.planes = []
        self.convertCoord(planesId, planesLon, planesLat)
        # 存储左下角飞机坐标
        self.edgePlane = Planes()
        self.findXYBorder()
        # 存储格子内的点
        self.grids = {}
        # 存储距离危险的点对
        self.dangers = {}

    # 分治 todo
    def divide(self, l, r, res):
        # 递归终止条件
        pass

    # 得到最近点对
    def getNearestPair(self) -> int:
        cnt = len(self.planes)
        # 若就一个点
        if cnt < 2:
            return 0
        # 随机初始化d
        self.randPlanesLists()
        d = self.getDistance(self.planes[0], self.planes[1])
        # 划分网格
        self.allocateGrid(d)
        for i in range(cnt):
            tempD = self.checkDistAround(self.planes[i], d)
            # 若有更小的d
            if tempD < d:
                d = tempD
                self.allocateGrid(d)
        return d

    # 检查该点周围是否有距离更小的点
    def checkDistAround(self, point: Planes, d: int) -> int:
        # 得到所在格子坐标
        x = (point.x - self.edgePlane.x) // d
        y = (point.y - self.edgePlane.y) // d
        delta = d
        for cnt in range(9):
            # 周围格子的坐标
            i = x + direct[cnt][0]
            j = y + direct[cnt][1]
            # 如果该格子内存在点
            if (i, j) in self.grids:
                for toPoint in self.grids[(i, j)]:
                    # 判断是否距离更近
                    # 跳过自身
                    if toPoint.planeId == point.planeId:
                        continue
                    temp = self.getDistance(point, toPoint)
                    delta = min(temp, delta)
                    if temp < 100:
                        # 按id升序配对
                        # 记录危险距离内的点对
                        self.dangers[tuple(sorted([point.planeId, toPoint.planeId]))] = temp
        return delta

    # 重新划分网格, 计算点所属格子
    def allocateGrid(self, d: int):
        for point in self.planes:
            x = (point.x - self.edgePlane.x) // d
            y = (point.y - self.edgePlane.y) // d
            if (x, y) in self.grids:
                self.grids[(x, y)].append(point)
            else:
                self.grids[(x, y)] = [point]

    # 排序, 找到网格左下边界
    def findXYBorder(self):
        # x的边界
        sortX = sorted(self.planes, key=lambda plane: plane.x)
        # y的边界
        sortY = sorted(self.planes, key=lambda plane: plane.y)
        self.edgePlane.x = sortX[0].x
        self.edgePlane.y = sortY[0].y

    # 随机打乱坐标点
    def randPlanesLists(self):
        random.shuffle(self.planes)

    # 计算两点间欧氏距离
    def getDistance(self, pA: Planes, pB: Planes) -> int:
        # 取整数, 可能损失了部分精度
        return int(round(math.sqrt((pA.x - pB.x) * (pA.x - pB.x) + (pA.y - pB.y) * (pA.y - pB.y))))

    # 将经纬度坐标转化为二维坐标
    def convertCoord(self, planesId, planesLon, planesLat):
        for i in range(len(planesId)):
            xy_coord = self.millerConvertionToXY(planesLon[i], planesLat[i])
            plane = Planes(planesId[i], xy_coord[0], xy_coord[1])
            self.planes.append(plane)

    # 采用Miller坐标系转换经纬度坐标
    def millerConvertionToXY(self, lon: float, lat: float) -> List[int]:
        """
        :param lon: 维度
        :param lat: 经度
        :return:
        """
        xy_coordinate = [0] * 2
        L = 6381372 * math.pi * 2  # 地球周长
        W = L  # 平面展开，将周长视为X轴
        H = L / 2  # Y轴约等于周长一般
        mill = 2.3  # 米勒投影中的一个常数，范围大约在正负2.3之间
        x = lon * math.pi / 180  # 将经度从度数转换为弧度
        y = lat * math.pi / 180  # 将纬度从度数转换为弧度
        y = 1.25 * math.log(math.tan(0.25 * math.pi + 0.4 * y))  # 米勒投影的转换
        # 这里将弧度转为实际距离
        x = (W / 2) + (W / (2 * math.pi)) * x
        y = (H / 2) - (H / (2 * mill)) * y
        # 返回整数
        xy_coordinate[0] = int(round(x))
        xy_coordinate[1] = int(round(y))
        return xy_coordinate


if __name__ == '__main__':
    test = AlgorithmHW3()
    d = test.getNearestPair()
    if len(test.dangers) == 0:
        print("此时, 飞机均在安全范围内...")
        print("最近点对距离为:", d)
    else:
        for key, val in test.dangers.items():
            print(f"飞机对{key}出现危险距离, 此时距离: {val}...")
        print("最近点对距离为:", d)



