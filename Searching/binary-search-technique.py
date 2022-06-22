# 정렬된 수열에서 원소 x의 개수를 찾는 함수 - O(logN)으로 동작
def count_by_value(array, x):
    n = len(array)
    a = first(array, x, 0, n-1)
    if a is None:
        return 0
    b = last(array, x, 0, n-1)
    return b - a + 1


# x의 첫번째 인덱스 리턴(없으면 None리턴)
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 가장 왼쪽에 있는 경우에만 인덱스 리턴
    if (mid == 0 or target > array[mid-1]) and target == array[mid]:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)

# x의 마지막 인덱스 리턴(없으면 None리턴)
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 가장 오른쪽에 있는 경우에만 인덱스 리턴
    if (mid == n-1 or target < array[mid+1]) and target == array[mid]:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)


n, x = map(int, input().split())
array = list(map(int, input().split()))
count = count_by_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)
    