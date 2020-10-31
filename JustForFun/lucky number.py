def lucky(num):
    sum2 = 0
    if num <= 0:
        print("Invalid input")
    else:
        for digit in str(num):
            sum2 = sum2 + int(digit)
        print(sum2)
        if sum2 % 2 == 0:
            return True
        else:
            return False


n = int(input('Enter the number'))
if lucky(n):
    print(n, " is lucky")
else:
    print(n, " is not lucky")
