"""二叉树的创建"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def print_tree(self):

        # 打印树的结构，先得到树的层数
        def get_layer(node):
            if node is None:
                return 0
            else:
                left_depth = get_layer(node.left)
                right_depth = get_layer(node.right) 
                return max(left_depth, right_depth) + 1

        layer = get_layer(self.__root)
        # 层序遍历并打印,deque 是 Python collections 模块里的双端队列，常用来当队列使用,创建一个队列，初始时放入根节点，并且记录根节点的深度为 1。
        queue = deque([(self.__root, 1)])
        current_level = 1
        while queue:
            node, level = queue.popleft()
            if level > current_level:
                print()
                current_level += 1
            if node:
                print(f"{node.data:^{20 * layer // 2 ** (level - 1)}}", end="")
            else:
                print(f"{"N":^{20 * layer // 2 ** (level - 1)}}", end="")
        if level < layer:
            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
            else:
                queue.append((None, level + 1))
                queue.append((None, level + 1))

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def search(self,item):
        return self.__search_pos(item)[0] is not None

    def __search_pos(self, item):
        parent = None
        current = self.__root
        while current:
            if current.data == item:
                break
            parent = current
            current = current.left if item < current.data else current.right
        return parent, current

