def merge(li, low, mid, high):
    i = low
    j = mid + 1
    list_tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            list_tmp.append(li[i])
            i += 1
        else:
            list_tmp.append(li[j])
            j += 1
    while i <= mid:
        list_tmp.append(li[i])
        i += 1
    while j <= high:
        list_tmp.append(li[j])
        j += 1
    li[low:high+1] = list_tmp

def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)

li = [5, 7, 2, 6, 9, 8, 1, 4, 0, 3]
print(li)
merge_sort(li, 0, len(li)-1)
print(li)