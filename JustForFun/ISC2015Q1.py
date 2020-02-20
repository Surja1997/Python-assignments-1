m = str(input("enter the number after which to be searched"))
n = int(input("enter the number which should be the sum of digits of the prev number entered"))
sum = 0
while True:
    for i in range(len(m)):
        sum += int(m[i])
    if sum == n:
        print("The number is\t", m)
        print("total number of digits is\t", len(m))
        exit()
    m = str(int(m) + 1)
    sum = 0
