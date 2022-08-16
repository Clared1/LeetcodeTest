from typing import List
from collections import defaultdict

class ContinuousDisjointSet:
    def __init__(self, data_list: List):
        # 初始化两个字典，分别保存节点的父节点（并查集）和保存父节点的大小
        self.fatherList = list(range(len(data_list)))
        for i in range(len(data_list)):
            # 强制插入顺利，避免产生环状结构
            # """
            # tmpmin = min(i, data_list[i])
            # tmpmax = max(i, data_list[i])
            # self.fatherList[tmpmin] = tmpmax
            # """
            self.union(i, data_list[i])

        # father_dict[i]表示节点i的父节点的index
        # self.size_dict = {}  # size_dict[i]表示节点i的后代节点个数
        # 初始化节点，将节点的父节点设为自身，size设为1
        # for node in data_list:
            # self.father_dict[node] = node
            # self.size_dict[node] = 1

    # 递归查找根节点（父节点是自己的节点）
    # 必须控制数据源是反向的，及不存在环的结构 1——2 ， 2——1,将进入死循环
    def findFather(self, index):
        # 获取节点的父节点
        father = self.fatherList[index]
        # 查找当前节点的父节点，直到父节点是其自己, 都从0开始计算，无论是index还是人
        if index != father:
            # 在降低树高优化时，确保父节点大小字典正确
            # 递归查找节点的父节点，直到根节点
            father = self.findFather(father)
        # 在查找父节点的时候，顺便把当前节点移动到父节点上面（优化操作）
        self.fatherList[index] = father
        return father

    # 查看两个节点是不是在一个集合里面
    def isSameFather(self, index1, index2):
        # 获取两个节点的父节点并比较父节点是否是同一个
        return self.findFather(index1) == self.findFather(index2)

    # 将两个集合合并在一起（只需合并根节点），size_dict大吃小（尽可能降低树高）
    def union(self, index1, index2):
        if index1 is None or index2 is None:
            return
        # 找到两个节点各自的根节点
        a_root = self.findFather(index1)
        b_root = self.findFather(index2)

        # 两个节点不在同一集合中，则合并两个集合
        if a_root != b_root:
            # 获取两个集合根节点的大小
            if a_root >= b_root:
                # 合并集合
                self.fatherList[b_root] = a_root
            else:
                # 合并集合
                self.fatherList[a_root] = b_root

    def getFatherList(self):
        for i in range(len(self.fatherList)):
            self.fatherList[i] = self.findFather(i)
        return self.fatherList



    def getMostFather(self):
        Fatherindex = []
        Fathernum = 0
        tmpdict = defaultdict(int)
        for i in range(len(self.fatherList)):
            tmpdict[self.findFather(i)] += 1
            if tmpdict[self.findFather(i)] > Fathernum:
                Fatherindex = [self.findFather(i)]
                Fathernum += 1
            elif tmpdict[self.findFather(i)] == Fathernum:
                Fatherindex.append(self.findFather(i))
        return Fatherindex, Fathernum


if __name__ == "__main__":
    tmp = ContinuousDisjointSet([0, 2, 1, 3])
    print(tmp.findFather(1))
    print(tmp.getFatherList())
    print(tmp.getMostFather())
    tmp.union(1, 3)
    print(tmp.findFather(2))
    print(tmp.getFatherList())
    print(tmp.getMostFather())


