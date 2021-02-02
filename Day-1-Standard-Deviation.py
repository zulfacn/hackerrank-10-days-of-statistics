# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
ar =  list(map(int, input().split()))
xx = 0 
phi = 0 
for k in range (0,n):
    xx = xx + ar[k]
for j in range (0,n):
    d = (ar[j] - (xx/n))**2
    phi = phi + d
sd = float((phi/n)**(1/2))
print(round(sd, 1))
