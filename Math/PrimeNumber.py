# 하나의 수에 대해서 소수 판별 알고리즘 
import math

def is_prime_number1(x): # O(x)
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def is_prime_number2(x): # O(x^(1/2))
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x))+ 1):
        if x % i == 0:
            return False
    return True

n = int(input())

print(is_prime_number1(n))
print(is_prime_number2(n))