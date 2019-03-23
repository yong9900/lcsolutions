n=int(input())

recieving={}
total_wait={}

time = 0
for i in range(n):
    mode, sec = input().split()
    num = int(sec)
    if mode == 'R':
        fnum = int
        recieving[num]=time
        time += 1
    elif mode == 'S':
        total_wait[num] = time-recieving[num]+total_wait.get(num, 0)
        recieving.pop(num, None)
        time += 1
    else: # mode is W
        time += num-1

for num in recieving:
    total_wait[num] = -1

for i in sorted(total_wait.keys()):
    print(i, total_wait[i])
