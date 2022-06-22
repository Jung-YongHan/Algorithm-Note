from bisect import bisect_left, bisect_right

# 정렬된 수열에 존재하는 x의 개수
def count_by_value(array, x):
    left_index = bisect_right(array, x)
    right_index = bisect_right(array, x)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))
count = count_by_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)    