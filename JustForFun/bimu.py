p = float(input("Enter the total no of plots"))
print("Enter numbers of each plot")
odd = 0
even = 0
for i in range(int(p)):
    data = float(input())
    if i % 2 == 0:
        even = even + data
    else:
        odd = odd + data
password = (odd + even) / 2
print(password)
