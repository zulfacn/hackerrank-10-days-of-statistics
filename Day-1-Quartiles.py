# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median
n  = int(input())
xx = [int(x) for x in input().split()]
xx.sort()
q = int(len(xx)/2)
if len(xx) % 2 == 0:
    L = xx[:q]
    U = xx[q:]
else :
    L = xx[:q]
    U = xx[q+1:]

print(int(median(L)))
print(int(median(xx)))
print(int(median(U)))
