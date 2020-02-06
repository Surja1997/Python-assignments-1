"""This program generates all possible numbers having only 2 unique digits, in ascending order.
    Ex- If nos are 7,8, the numbers generated are 7,8,77,78,87,88... etc upto n results.
    date- 1/2/19
    -Surjashish
"""


def numPlay(a, b, n):
    list = [str(a), str(b)]
    listTemp = []
    listTemp2 = []
    k = 7
    while len(list) <= n:
        if len(list) == 2:
            if k == 7:
                for nums in list:
                    listTemp.append(str(k) + nums)
                k = 8
            if k == 8:
                for nums in list:
                    listTemp.append(str(k) + nums)
                k = 7
        else:
            if k == 7:
                for nums in listTemp:
                    listTemp2.append(str(k) + nums)
                k = 8
            if k == 8:
                for nums in listTemp:
                    listTemp2.append(str(k) + nums)
                k = 7
            listTemp = listTemp2.copy()
            listTemp2.clear()

        list = list + listTemp
    print(list[:n])


numPlay(7, 8, 200)
