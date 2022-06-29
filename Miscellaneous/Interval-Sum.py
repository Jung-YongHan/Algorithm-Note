# 수열의 특정 구간 내의 합을 빠르게 구하는 알고리즘
# 접두사 합(Prefix Sum - 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것)을 이용한 알고리즘이다.
array = list(map(int, input().split()))

sum = 0
prefix_sum = [0]
for i in array:
    sum += i
    prefix_sum.append(sum)

for j in range(int(input())):
    left, right = map(int, input().split())
    print(prefix_sum[right] - prefix_sum[left - 1])