t = int(input())
for i in range(t):
    n = int(input())
    coin5 = 0
    coin10 = 0
    coin15 = 0
    sale = list(map(int, input().split()))
    asale = 1
    for j in range(len(sale)):
        if sale[j] == 5:
            coin5 = coin5+1
        elif sale[j] == 10:
            if coin5 > 0:
                coin5 = coin5 - 1
                coin10 = coin10 + 1
            else:
                asale = 0
                break
        else:
            if sale[j] == 15:
                if coin10 > 0:
                    coin10 = coin10 - 1
                    coin15 = coin15 + 1
                elif coin5 >= 2:
                    coin5 = coin5 - 2
                    coin15 = coin15 + 1
                else:
                    asale = 0
                    break
    if asale == 1:
        print('YES')
    else:
        print('NO')
