"""This program generates all possible numbers having only 2 unique digits, in ascending order.
    Ex- If nos are 7,8, the numbers generated are 7,8,77,78,87,88... etc. upto n results. (With greater computation time)
    date- 1/2/19
    -Surjashish
"""


def numPlay(a, b, n):
    listNums = []
    condition = True
    x = 1
    while len(listNums) <= n - 1:
        numAsStr = str(x)
        for y in range(len(numAsStr)):
            if numAsStr[y] != str(a) and numAsStr[y] != str(b):
                condition = False

        if condition:
            listNums.append(x)
        condition = True
        x += 1

    print(listNums)


numPlay(7, 8, 200)
