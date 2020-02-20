a = 5
for row in range(a):
    print("*", end=" ")
print()
for col in range(a - 1):
    for spaces in range(int(abs(a / 2)) + 2):
        print(" ", end="")
    print("*")
for row in range(int(abs(a / 2)) + 1):
    print("*", end=" ")
print()

result_str = "";
for row in range(0, 7):
    for column in range(0, 7):
        if ((row == 0 or row == 3 or row == 6) and 1 < column < 5) or (
                column == 1 and (row == 1 or row == 2 or row == 6)) or (
                column == 5 and (row == 0 or row == 4 or row == 5)):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str);
