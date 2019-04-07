num = int(input())

names1 = input().split()
names2 = input().split()

mapping = {}
is_good = True
for i in range(num):
    if names1[i] == names2[i]:
        is_good = False
        break
    if names1[i] in mapping:
        if names2[i] != mapping[names1[i]]:
            is_good = False
            break
    else:
        mapping[names1[i]] = names2[i]

if is_good:
    print("good")
else:
    print("bad")    

