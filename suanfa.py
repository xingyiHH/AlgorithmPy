def buddle_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        low  = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]
        return quick_sort(low) + [pivot] + quick_sort(high)

# 递归思想的二分查找
def binary_search(alist,item):
    n = len(alist)
    if n>0:
        mid = n//2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            return binary_search(alist[mid+1:],item)
        else:
            return binary_search(alist[:mid],item)
    return False

# 非递归思想的二分查找
def binary_search_1(alist,item):
    n = len(alist)
    first = 0
    last = n-1
    while first <=last:
        mid = (first+last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            first = mid+1
        else:
            last = mid -1
    return False


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr1 = [17.20,26,31,34,44,54,55,77,93]
    budddlesortList = buddle_sort(arr)
    quicksortList = quick_sort(arr)
    binarysearchEnum = binary_search(arr1,87)
    binarysearchEnum1 = binary_search_1(arr1,87)
    print(budddlesortList)
    print(quicksortList)
    print(binarysearchEnum)
    print(binarysearchEnum1)
    #hhhhh