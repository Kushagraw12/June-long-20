T = int(input())
a = []
for i in range(T):
    s = str(input())
    an = 0
    j = 0
    while True:
        if j >= len(s) - 1:
            break
        if s[j+1] != s[j]:
            an += 1
            j += 1
        if j >= len(s) - 1:
            break
        j += 1
    a.append(an)
for i in range(len(a)):
    print(a[i])
