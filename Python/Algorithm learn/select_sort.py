# 从小到大进行选择排序
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i, len(li)-1):
            if li[j] < li[i]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

list = [8, 7, 1, 5, 9, 4, 2, 3, 6]
print(list)
select_sort(list)
print(list)
