# 수열의 최댓값이 10,000이하라 가정
# O(N+K)의 시간 복잡도로 작동 N은 수의 개수, 수열의 가능한 최댓값 K
# 수열 내의 수들의 중복이 많고 수의 최댓값이 크지 않을 시에 적용

arr = list(map(int, input().split()))
dp = [0] * 10001
for i in arr:
    dp[i] += 1
    
for j in range(len(dp)):
    if dp[j] >= 1:
        for k in range(dp[j]):
            print(j, end=' ')