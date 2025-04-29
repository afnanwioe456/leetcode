import numpy as np


class TreeNode:
    def __init__(self, coord: list, item):
        self.coord = coord
        self.value = item
        self.dim = 0
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class KDTree:
    def __init__(self, dims):
        self.dims = dims
        self.root: TreeNode | None = None
        self._closest_dis_square = float('inf')

    def _next_dim(self, d):
        if d == self.dims - 1:
            return 0
        return d + 1

    def _add_recursively(self, node: TreeNode, new_node: TreeNode):
        cur_dim = node.dim
        if new_node.coord[cur_dim] < node.coord[cur_dim]:
            p = node.left
            if not p:
                new_node.dim = self._next_dim(cur_dim)
                node.left = new_node
                return
        else:
            p = node.right
            if not p:
                new_node.dim = self._next_dim(cur_dim)
                node.right = new_node
                return
        return self._add_recursively(p, new_node)

    def add(self, coord: list, item):
        node = TreeNode(coord, item)
        if not self.root:
            self.root = node
            return
        self._add_recursively(self.root, node)

    @staticmethod
    def _distance_square(c1, c2):
        return np.sum((np.array(c1) - np.array(c2)) ** 2)

    def _closest_traversal(self, node: TreeNode | None, coord: list):
        if not node:
            return None, None
        dis = self._distance_square(node.coord, coord)
        res = node
        if dis < self._closest_dis_square:
            self._closest_dis_square = dis
        cur_dim = node.dim
        if coord[cur_dim] < node.coord[cur_dim]:
            n_1, d_1 = self._closest_traversal(node.left, coord)
            if abs(coord[cur_dim] - node.coord[cur_dim]) <= self._closest_dis_square:
                n_2, d_2 = self._closest_traversal(node.right, coord)
            else:
                n_2, d_2 = None, None
        else:
            n_1, d_1 = self._closest_traversal(node.right, coord)
            if abs(coord[cur_dim] - node.coord[cur_dim]) <= self._closest_dis_square:
                n_2, d_2 = self._closest_traversal(node.left, coord)
            else:
                n_2, d_2 = None, None
        if n_1 and d_1 < dis:
            dis = d_1
            res = n_1
        if n_2 and d_2 < dis:
            dis = d_2
            res = d_2
        return res, dis

    def closest(self, coord):
        if not self.root:
            return
        self._closest_dis_square = float('inf')
        res, _ = self._closest_traversal(self.root, coord)
        return res.value


if __name__ == '__main__':
    tree = KDTree(2)
    tree.add([2, 3], 'A')
    tree.add([4, 2], 'B')
    tree.add([4, 5], 'C')
    tree.add([3, 3], 'D')
    tree.add([1, 5], 'E')
    tree.add([4, 4], 'F')
    print(tree.closest([0, 3]))


