# Enter your code here. Read input from STDIN. Print output to STDOUT
#input p and n 
INPUT = list(map(int, input().split()))
p = INPUT[0] / INPUT[1]
n = int(input())

#print output
print(round((1-p)**(n-1)* p, 3))
