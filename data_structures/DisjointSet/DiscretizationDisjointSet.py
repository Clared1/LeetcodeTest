from typing import Sequence


class DiscretizationDisjointSet:
    def __init__(self, data_list: Sequence):
        # 初始化两个字典，分别保存节点的父节点（并查集）和保存父节点的大小
        self.father_dict = {}  # father_dict[i]表示节点i的父节点
        self.size_dict = {}  # size_dict[i]表示节点i的后代节点个数
        # 初始化节点，将节点的父节点设为自身，size设为1
        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    # 递归查找根节点（父节点是自己的节点）
    def findFather(self, node):
        # 获取节点的父节点
        father = self.father_dict[node]
        # 查找当前节点的父节点，直到父节点是其自己
        if node != father:
            # 在降低树高优化时，确保父节点大小字典正确
            if father != self.father_dict[father]:
                self.size_dict[father] -= 1
            # 递归查找节点的父节点，直到根节点
            father = self.findFather(father)
        # 在查找父节点的时候，顺便把当前节点移动到父节点上面（优化操作）
        self.father_dict[node] = father
        return father

    # 查看两个节点是不是在一个集合里面
    def isSameFather(self, node_a, node_b):
        # 获取两个节点的父节点并比较父节点是否是同一个
        return self.findFather(node_a) == self.findFather(node_b)

    # 将两个集合合并在一起（只需合并根节点），size_dict大吃小（尽可能降低树高）
    def union(self, node_a, node_b):
        if node_a is None or node_b is None:
            return
        # 找到两个节点各自的根节点
        a_root = self.findFather(node_a)
        b_root = self.findFather(node_b)

        # 两个节点不在同一集合中，则合并两个集合
        if a_root != b_root:
            # 获取两个集合根节点的大小
            a_set_size = self.size_dict[a_root]
            b_set_size = self.size_dict[b_root]
            # 判断两个集合根节点大小，并进行合并（大吃小）
            if a_set_size >= b_set_size:
                # 合并集合
                self.father_dict[b_root] = a_root
                # 更新大小
                self.size_dict[a_root] = a_set_size + b_set_size
            else:
                # 合并集合
                self.father_dict[a_root] = b_root
                # 更新大小
                self.size_dict[b_root] = a_set_size + b_set_size


if __name__ == "__main__":
    tmp = DiscretizationDisjointSet([1, 2, 3, 4])
    tmp.union(1, 2)
    tmp.union(3, 4)
    print(tmp.findFather(1))
    print(tmp.findFather(2))


