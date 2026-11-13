# 该案例演示了算法的时间复杂度
# 对表中的元素进行求和

import time


def my_sum(nums):
    # start_time = time.perf_counter()
    sum_num = 0  # 1次赋值
    for num in nums:
        sum_num += num
    # end_time = time.perf_counter()
    # print(f"总耗时 {end_time - start_time:.6f} 秒")
    return sum_num


nums = [i for i in range(1000)]
print(my_sum(nums))


# 找出列表中的元素最大值
def find_max(nums):
    max_num = nums[0]
    i = 0
    while (i := i + 1) < len(nums):
        if nums[i] > max_num:
            max_num = nums[i]
    return max_num
 

print(find_max([2, 8, 5, 10]))
