t = int(input())
for i in range(t):
    n = int(input())
    helper = [k for k in range(1, n*n+1)]
    M = []
    for m in range(n):
        a = []
        for c in range(n):
            if n % 2 == 0 and m % 2 != 0:
                help = helper[(m*n)+n-c-1]
                a.append(help)
            else:
                help = helper[(m*n) + c]
                a.append(help)
        M.append(a)
    for l in range(n):
        for e in range(n):
            print(str(M[l][e]), end=" ")
        print()
