# functions
def FACTORIAL(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return FACTORIAL(n - 1) * n

def BINOMIAL(x, n, p):
    F = FACTORIAL(n) / (FACTORIAL(n - x) * FACTORIAL(x))
    return (F * p**x * (1.0 - p)**(n-x))

#dataset
VALUES = list(map(float, input().split()))
p = VALUES[0] / (VALUES[0] + VALUES[1])
n = 6

# Get binomial result
RESULT = BINOMIAL(3,n,p) + BINOMIAL(4,n,p) + BINOMIAL(5,n,p) + BINOMIAL(6,n,p)
print(round(RESULT, 3))
