# 매번 가장 작은 것을 선택하여 정렬
arr = list(map(int, input().split()))
n = len(arr)
for i in range(n-1):
    min_index = i
    for j in range(i, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print(*arr)