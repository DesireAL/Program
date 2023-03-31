# 从小到大进行堆排序 好难啊
def sift(li, low, high):    # 向下调整  low为父节点 high为元素量
    i = low     # 最开始指向根节点(tmp要去的位置)
    j = 2 * i + 1   # 左节点
    tmp = li[low]   # 把堆顶i位置的数存起来
    while j <= high:    # j位置有数时
        if j + 1 <= high and li[j+1] > li[j]:   # 存在右节点且比左节点大
            j = j + 1   # j指向右节点
        if li[j] > tmp:
            li[i] = li[j]
            i = j       # i与j换下一行
            j = 2 * i + 1
        else:
            li[i] = tmp     # 子节点均比父节点小时，父节点(li[i]空位)=tmp
            break
    else:
        li[i] = tmp     # j超出high值后，li[i]的空位=tmp

def heap_sort(li):
    n = len(li)-1     # n为列表长度-1(列表下标从0开始)
    for i in range((n-1)//2, -1, -1):       # i为父节点的下标(从下到上，也就是从列表的右到左),循环后构建堆
        sift(li, i, n)
    print(li,'>>>>将列表进行堆排序')
    for i in range(n, -1, -1):        # 将堆进行排序
        li[0], li[i] = li[i], li[0]     # 将根节点与未排序列表的最后位置交换
        sift(li, 0, i - 1)      # 0为low，也就是根节点，i-1为high，也就是未排序列表的最后一位，-1是因为i，也就是n(原列表最后一位)已经与根节点交换了
    print(li,'>>>>将列表进行堆排序完')

li = [7, 9, 6, 1, 3, 2, 5, 8, 0, 4]
print(li)
heap_sort(li)