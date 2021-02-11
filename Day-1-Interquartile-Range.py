# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st 

n = int(input())
element = list(map(int, input().split()))
freq = list(map(int, input().split()))

S = []
for i in range(n):
    S += [element[i]] * freq[i]
N = sum(freq)
S.sort()

if n%2 != 0:
    Q1 = st.median(S[:N//2])
    Q3 = st.median(S[N//2+1:])
else:
    Q1 = st.median(S[:N//2])
    Q3 = st.median(S[N//2:])

IQR = round(float(Q3 - Q1), 1)
print(IQR)
