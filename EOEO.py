# cook your dish here
t = int(input())
for i in range(t):
    ts = int(input())
    if ts % 2 == 0:
        while(ts % 2 == 0):
            ts = ts // 2
        j = (ts - 1) // 2
    else:
        j = (ts - 1) // 2
    print(j)
