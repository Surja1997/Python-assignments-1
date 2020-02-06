"""This program generates a circular pattern for any number entered.
    The pattern starts from 1 and ends at that number.
    date- 1/2/19
    -Surjashish
"""


def circular(n):
    side, count, case = 2, 1, 1

    for x in range(2, 100):
        if n <= 4:
            side = 2
        elif n == x ** 2:
            side = x
        elif x ** 2 < n < (x + 1) ** 2:
            side = x + 1
    arr = [[0 for x in range(side)] for y in range(side)]

    i, j, k, l = 0, side, 0, side
    while count <= n:
        if case == 1:  # right
            for x in range(i, j):
                if count <= n:
                    arr[k][x] = count
                    count += 1
            k += 1
            case = 2
        if case == 2:  # down
            for x in range(k, l):
                if count <= n:
                    arr[x][j - 1] = count
                    count += 1
            j -= 1

            case = 3
        if case == 3:  # left
            for x in range(l - 2, i, -1):
                if count <= n:
                    arr[l - 1][x] = count
                    count += 1
            l -= 1
            case = 4
        if case == 4:  # up
            for x in range(l, i, -1):
                if count <= n:
                    arr[x][i] = count
                    count += 1
            case = 1
            i += 1

    for x in range(side):
        for y in range(side):
            if arr[x][y] != 0:
                print(arr[x][y], end="\t")
            else:
                print("\t", end="")
        print()


circular(100)
