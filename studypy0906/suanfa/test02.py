#  该案例自定义数组数据结构

class MyArray:
    def __init__(self):
        # 容量
        self.__capacity = 8
        # 数组中的元素个数
        self.__size = 0
        # 存放数组中的元素容器
        self.__items = [0] * self.__capacity

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __str__(self):
        res_str = "["
        for i in range(self.size):
            res_str += str(self.__items[i])
        res_str += "]"
        return res_str


class Node:
    # 链表节点类
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        # 链表的头节点
        self.__head = None
        self.__size = 0

    def __str__(self):
        # 输出链表上的数据
        res_list = []

        # 遍历链表上的所有节点
        current = self.__head
        while current:
            res_list.append(str(current.data))
            current = current.next
        return "->".join(res_list)

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def insert(self, index, item):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        """判断是否是添加的头结点"""
        if index == 0:
            self.__head = Node(item, self.__head)

        else:
            # 插入到中间，先找到index-1位置的节点
            node = self.__head
            for i in range(index - 1):
                node = node.next

            node.next = Node(item, node.next)

        self.__size += 1

    def set(self, index, item):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        node = self.__head
        for i in range(index):
            node = node.next

        node.data = item

    def get(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("index out of range")

        node = self.__head
        for i in range(index):
            node = node.next
        return node.data

    def find(self, item):
        # node = self.__head
        # while node:
        #     if node.data == item:
        #         return True
        #     node = node.next
        # return False
    #查找元素在链表上第一次出现的下标位置
        node = self.__head
        for i in range(self.__size):
            if node.data == item:
                return i
            node = node.next
        return -1

# my_list = LinkedList()
# node1 = Node(1, my_list)
# node2 = Node(2, my_list)

# print(my_list)
