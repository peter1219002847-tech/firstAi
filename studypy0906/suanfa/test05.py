"""
该案例演示了哈希表的实现

"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.__capacity = 8  # 数组长度
        self.__size = 0  # 键值对个数
        self.__load_factor = 0.7  # 负载因子
        """
        创建一个长度为 capacity 的列表，每个元素都是 None。
        这就是底层存储桶的数组。每个桶可以存放一个链表（或节点），初始时都是空
        """
        self.__table = [None] * self.__capacity

    def display(self):
        for i, node in enumerate(self.__table):
            print(i, node)
            current = node
            while current:
                print(f"{current.key} --> {current.value}", end="")
                current = current.next
            print("None")
        print("结束")

    def __hash(self, key):
        return hash(key) % self.__capacity

    def __grow(self):
        self.__capacity = self.__capacity * 2
        self.__table,old_table = [None] * self.__capacity,self.__table
        self.__size = 0

        # 将旧哈希表中的元素重新插入到新的哈希表中
        for node in old_table:
            current = node
            while current:
                self.put(current.key, current.value)
                current = current.next

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def put(self, key, value):

        # 如果负载因子超过阈值则进行扩容
        if self.__size / self.__capacity > self.__load_factor:
            self.__grow()

        index = self.__hash(key)
        new_node = Node(key, value)
        #如果当前位置为空，直接插入
        if self.__table[index] is None:
            self.__table[index] = new_node
        else:
            #否则，发生哈希冲突、链式存储
            current = self.__table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            #如果键不存在，插入到链表尾部
            current.next = new_node
        self.__size += 1

    def remove(self, key):
        """删除键值对"""
        index = self.__hash(key)
        current = self.__table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    #删除非头节点
                    prev.next = current.next
                else:
                    self.__table[index] = current.next
                self.__size -= 1
                return True
            prev = current
            current = current.next
        return False

    def get(self, key):
        #访问键值对
        index = self.__hash(key)
        current = self.__table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None


