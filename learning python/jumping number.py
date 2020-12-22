c, k = 0, 0
while k < 101:
    if len(str(c)) == 1:
        print(c)
        c += 1
        k += 1
    if len(str(c)) == 2:
        if int(str(c)[0]) == int(str(c)[1])-1 or int(str(c)[0]) == int(str(c)[1])+1:
            print(c)
            c += 1
            k += 1
        else:
            c += 1
    else:
        jump = False
        num = str(c)
        num_len = len(num)
        jump = False
        for i in range(1, num_len - 1):
            if int(num[i]) == (int(num[i - 1]) + 1) or int(num[i]) == (int(num[i - 1]) - 1):
                jump = True
            else:
                jump = False
            if int(num[i]) == (int(num[i + 1]) - 1) or int(num[i]) == (int(num[i + 1]) - 1):
                jump = True
            else:
                jump = False
        c += 1
        if jump:
            print(num)
            k += 1


