# Enter your code here. Read input from STDIN. Print output to STDOUT
def FACTORIAL(n):
    return 1 if n == 0 else n*FACTORIAL(n-1)
def COMBINATION(n, x):
    return FACTORIAL(n) / (FACTORIAL(x) * FACTORIAL(n-x))
def BINOMIAL(n, p, x):
    return COMBINATION (n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([BINOMIAL(i, n, p/100) for i in range(3)]), 3))
print(round(sum([BINOMIAL(i, n, p/100) for i in range(2, n+1)]), 3))
