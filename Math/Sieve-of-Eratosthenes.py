# 특정한 수의 범위 안에 존재하는 모든 소수를 찾는 알고리즘 O(XloglogX) (거의 선형시간에 가까움)
# 그러나 수가 매우 커질 경우 메모리의 효율성이 안 좋아진다.
import math

x = int(input())
array = [True for _ in range(x+1)]
for i in range(2, int(math.sqrt(x)) + 1):
    if array[i]:
        j = 2
        while i*j <= x:
            array[i*j] = False
            j += 1

for i in range(2, x+1):
    if array[i]:
        print(i)