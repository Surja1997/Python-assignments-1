a = [2, 3, 4, 1, 5, 7, 9, 11, 2, 4, 5, 23, 44, 66, 77, 2]
listTemp = []
list = []
k = 0
while k < len(a) - 1:
    if a[k + 1] > a[k]:
        if len(listTemp) > 0:
            listTemp.append(a[k + 1])
        else:
            listTemp.append(a[k])
            listTemp.append(a[k + 1])
        if len(listTemp) > len(list):
            list.clear()
            list = listTemp.copy()
    else:
        listTemp.clear()
    k += 1
print(list)
