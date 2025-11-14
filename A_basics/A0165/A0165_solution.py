# A0165 - جایگشت nPr

def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutation(n, r):
    if r > n or r < 0:
        return 0
    return factorial(n) // factorial(n - r)

n = int(input())
r = int(input())

print(permutation(n, r))
