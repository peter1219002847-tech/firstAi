class MyStack:
    def __init__(self):
        self.__size = 0
        self.__item = []

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def push(self, item):
        self.__item.append(item)

    def pop(self):
        if(self.is_empty()):
            raise IndexError("Stack is empty")
        # 返回栈顶元素并删除
        # return self.__item.pop()
        item = self.__item[self.__size - 1]
        del self.__item[self.__size - 1]
        self.__size -= 1
        return item
    def peek(self):
        # 返回栈顶元素
        return self.__item[self.__size - 1]

ms = MyStack()
ms.push(1)
ms.push(2)
ms.push(3)


print(ms.peek())
print(ms.pop())
print(ms.pop())
print(ms.pop())
print(ms.pop())
