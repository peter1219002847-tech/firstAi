# 该案例演示了防止函数对list表数据进行修改
def change_list(list1):
    print(f"list1: {list1},地址是{id(list1)}")
    list1.append(100)
    print(f"修改后{list1},地址是{id(list1)}")

list2 = [1, 2, 3]
change_list(list2)
