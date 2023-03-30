# 从小打大进行冒泡排序
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[j] < li[i]:
                li[j], li[i] = li[i], li[j]

list = [3, 7, 6, 9, 5, 2, 1, 8, 4]
print(list)
bubble_sort(list)
print(list)