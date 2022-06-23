arr = list(map(int, input().split()))

def quick_sort1(arr, low, high): # in-placing
    if low >= high:
        return 
    pivot = low
    left = low+1
    right = high
    while left <= right:
        while left <= high and arr[left] <= arr[pivot]:
            left += 1
        while right > low and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort1(arr, low, right-1)
    quick_sort1(arr, right+1, high)

# def quick_sort2(arr): # not in-placing
#     if len(arr) <= 1:
#         return arr
#     pivot = len(arr) // 2
#     left_arr = [x for x in arr if x < arr[pivot]]
#     right_arr = [x for x in arr if x > arr[pivot]]
#     return quick_sort2(left_arr) + [arr[pivot]] + quick_sort2(right_arr)

quick_sort1(arr, 0, len(arr)-1)
# quick_sort2(arr)
print(*arr)
