# Enter your code here. Read input from STDIN. Print output to STDOUT
#Input
N = int(input())
number = list(map(int, input().split()))

#Mean
Sum = 0
for i in number:
    Sum = Sum + i 
print(float(Sum / N ))

#median
numbers = sorted(number)
if  N % 2 == 0 :
    median_1 = numbers[N//2]
    median2 = numbers[N//2 - 1]
    median = (median_1 + median2) / 2
else :
    median  = numbers[N//2]
print(median)

#mode
maks = 0

for i in numbers :
    counter = 0 
    indeks = numbers.index(i)
    
    for j in range(indeks, len(numbers)):
        if i == numbers[j]:
            counter = counter + 1
        if counter > maks:
            maks = counter 
            if maks == 1:
                mode = numbers[0]
            else :
                mode = i
print (mode)
