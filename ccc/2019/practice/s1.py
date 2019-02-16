days = int(input())
s1 = map(int, input().split(' '))
s2 = map(int, input().split(' '))

ld = 0
count=0
sum1, sum2 = 0, 0
for i, j in zip(s1,s2):
    count+=1
    sum1+=i
    sum2+=j
    if sum1==sum2:
        ld = count

print(ld)

