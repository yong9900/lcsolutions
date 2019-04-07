a=[]
for i in range(4):
    a.append([int(j) for j in input().split()])
sum = 0
for i in range(4):
    sum += a[0][i]
    
isMagic = True
for i in range(4):
    my = 0
    for j in range(4):
        my += a[i][j]
    if my != sum:
        isMagic = False

for i in range(4):
    my = 0
    for j in range(4):
        my += a[j][i]
    if my != sum:
        isMagic = False

if isMagic:
    print("magic")
else:
    print("not magic")

#read the string
s = input()
l = len(s)

ans = 1 #the len is at least 1
#check if we have palindrome centered by a charactor
#like this: "ABA", "AABAACD"
for i in range(l):
    j=0
    #need to check s[i-j] and s[i+j]
    #but need to make sure i-j and i+j are within the string
    while i-j>=0 and i+j<l:
        if s[i-j]==s[i+j]:
            ans=max(ans, 2*j+1)
            j=j+1
        else:
            break

#check if we have palindrome centered by in between two charactors
#like this: "ABBA", "AABBAACD"
for i in range(l-1):
    j=0
    #need to check s[i-j] and s[i+1+j]
    #but need to make sure i-j and i+j are within the string
    while i-j>=0 and i+1+j<l:
        if s[i-j]==s[i+1+j]:
            if ans < 2*j+2:
                ans = 2*j+2 
            ans=max(ans, 2*j+2)
            j=j+1
        else:
            break

print(ans)