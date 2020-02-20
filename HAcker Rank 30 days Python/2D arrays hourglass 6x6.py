arr = []
for x in range(6):
    list_temp = []
    for x1 in str(input()).split(" "):
        list_temp.append(int(x1))
    arr.append(list_temp)
k = 0
sum_arr, sum_arr_temp = 0, 0
while k < 4:

    print(arr)
    print("============================")
    for i in range(4):
        sum_arr_temp = arr[0][i] + arr[0][i + 1] + arr[0][i + 2] + arr[1][i + 1] + arr[2][i] + arr[2][i + 1] + arr[2][i + 2]
        print("temp = ",sum_arr_temp)
        if sum_arr_temp > sum_arr:
            sum_arr = sum_arr_temp
        sum_arr_temp = 0
    arr2 = arr[1:]
    arr2.append(arr[0])
    arr = arr2
    k += 1
print("max=", sum_arr)
