# 从小到大进行插入排序
def insert_sort(li):
    for i in range(1, len(li)):     # 从列表中按顺序抽值
        tmp = li[i]                 # 记录下抽出值的大小
        j = i - 1                   # 依次对抽出的值左边的值进行比较
        while li[j] > tmp and j >= 0:       # 当左边的值大于抽出的值时
            li[j+1] = li[j]                 # 将左边的值右移一位
            j -= 1                          # 判断下一位
        li[j+1] = tmp                       # 当左边的值不大于抽出的值时，将抽出的值填入空位

list = [5, 7, 9, 3, 1, 2, 8, 6, 4]
print(list)
insert_sort(list)
print(list)