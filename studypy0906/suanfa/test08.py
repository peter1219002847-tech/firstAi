"""归并排序"""


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

# arr要处理的数组
# n数组中的元素个数
# i堆化的节点
def heapify(arr, n, i):
    largest = i
    # 获取当前处理的节点的左子节点下标
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if largest != i:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n=len(arr)
    # 获取最后一个非叶子节点
    last_idx = n // 2 - 1
    # 从最后一个非叶子节点自底向上堆花
    for i in range(last_idx, -1, -1):
        heapify(arr, n, i)

    for j in range(n - 1, 0, -1):
        # 交换堆顶和堆底
        arr[0], arr[j] = arr[j], arr[0]
        # 重新堆化，自顶向下
        heapify(arr, j, 0)
    return arr

print(heap_sort([5,6,8,1,2,3,4]))