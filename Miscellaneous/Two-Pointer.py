# 수열 내의 부분합을 만족하는 연속 부분 수열의 개수를 찾는 알고리즘
# 수열 내의 원소가 모드 자연수일 때 사용가능

# 각, 원소의 개수, 부분 합
n, m = map(int, input().split())
array = list(map(int, input().split())) # 수열

count = 0
interval_sum = 0
end = 0
for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += array[end]
        end += 1
    if interval_sum == m:
        count +=  1
    interval_sum -= array[start]

print(count)