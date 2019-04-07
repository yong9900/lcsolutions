
i = int(input())

count=0

for j in range(1, 6):
    if i<j:
        continue
    if i==j:
        count+=1
    else:
        k=i-j
        if k<6 and k>=j:
            count+=1

print(count) 