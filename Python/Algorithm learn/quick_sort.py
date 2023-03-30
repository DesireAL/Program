# 从小打到进行快速排序
def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)

def partition(li, left, right):
    tem = li[left]
    while left < right:     # 说明有两个以上的元素
        while left < right and li[right] >= tem:        # 当右边的元素大于抽出的元素时
            right -= 1                                  # 右边下标往左走一步
        li[left] = li[right]                        # 如果右边元素小于抽出元素，则放入left的空位
        #print(list, 'right')
        while left < right and li[left] <= tem:         # 当左边的元素小于抽出的元素时
            left += 1                                   # 左边下标往右走一步
        li[right] = li[left]                        # 如果左边元素大于抽出元素，则放入right的空位
        #print(list, 'left')
    li[left] = tem
    return left

list = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print(list)
quick_sort(list, 0, len(list)-1)
print(list)