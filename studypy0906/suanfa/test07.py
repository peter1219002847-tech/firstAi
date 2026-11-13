"""
二分查找法、摩尔投票算法
"""


def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        # 获取中间索引
        mid = (start + end) // 2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] < target):
            start = mid + 1
        else:
            end = mid - 1

    return -1


print(binary_search([1, 2, 3, 4, 5], 5))


def majorityElement(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


print(majorityElement([2, 2, 2, 1, 1, 1]))


# 冒泡排序
# 初始：[5, 3, 8, 1]
# 第 1 轮（i = 0）：
# 比较 5 和 3，交换 → [3, 5, 8, 1]
# 比较 5 和 8，不交换 → [3, 5, 8, 1]
# 比较 8 和 1，交换 → [3, 5, 1, 8]
# 此时最大的 8 已经排到最后。
# 第 2 轮（i = 1）：
# 比较 3 和 5，不交换 → [3, 5, 1, 8]
# 比较 5 和 1，交换 → [3, 1, 5, 8]
# 此时 5 排到倒数第二位。
# 第 3 轮（i = 2）：
# 比较 3 和 1，交换 → [1, 3, 5, 8]
# 排序完成，返回 [1, 3, 5, 8]。
def bubble_sort(arr):
    n = len(arr)
    # 比较的轮数
    for i in range(n - 1):
        # 每轮比较的次数
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                #两两比较交换顺序
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([3, 1, 6, 2, 5]))
