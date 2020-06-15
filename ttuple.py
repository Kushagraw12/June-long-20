import sys
import heapq
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(0, t):
        # a = []
        d = 0
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        x = b[0] - a[0]
        y = b[1] - a[1]
        z = b[2] - a[2]
        if a[0] != 0:
            l = b[0] / a[0]
        if a[1] != 0:
            m = b[1] / a[1]
        if a[2] != 0:
            n = b[2] / a[2]
            u = b[0] % a[0]
        v = b[1] % a[1]
        w = b[2] % a[2]
        if (x == y and y == z and z == 0):
            d += 0
        elif (x == y and y == z) or (x == y and z == 0) or (y == z and x == 0) or (z == x and y == 0):
            d += 1
        elif (x == y and y == 0 and z != 0) or (x == z and z == 0 and y != 0) or (z == y and y == 0 and x != 0) or (l == m and m == n and u == v and v == w and w == 0):
            d += 1
        elif ((l == m and n == 1) or (l == n and m == 1) or (n == m and l == 1) or (l == m and n != 1 and m == 1) or (l == n and m != 1 and l == 1) or (n == m and l != 1 and n == 1)) and (u == v and v == w and w == 0):
            d += 1
        elif (y == (x+z)) or (x == (y+z)) or (z == (x+y)) or ((l == (m*n)) and (u == v and v == w and w == 0)) or ((m == (l*n)) and (u == v and v == w and w == 0)) or ((n == (l*m)) and (u == v and v == w and w == 0)):
            d += 2
        elif (x == y and z != 0) or (y == z and x != 0) or (z == x and y != 0) or (l == (m) and n != 1 and (u == v and v == w and w == 0)) or (m == (n) and l != 1 and (u == v and v == w and w == 0)) or (n == (l) and m != 1 and (u == v and v == w and w == 0)):
            d += 2
        elif (x != y and z == 0) or (y != z and x == 0) or (z != x and y == 0):
            d += 2
        print(d)
    return 0


if __name__ == "__main__":
    main()
