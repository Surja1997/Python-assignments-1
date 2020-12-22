if 5 > 2:
    print("5 is greater than 2")

# unpack a collection
fruits = ["apple", "banana", "orange"]
x, y, z = fruits

# difference between + and ,
print(x, y, z)
print(x + y + z)

print(fruits[0], "are tasty")

print(fruits[0], 5)


# global variable
def my_func():
    global y
    y = "awesome"


my_func()
print(y)

# changing value of a global variable
name = "Mohor"

print("original name = " + name)


def change_name():
    global name
    name = "surjashish"


change_name()
print("new name is " + name)

# sample prg to separate even and odd nos

a = [2, 54, 265, 854, 24, 88, 44, 77, 3, 582, 235, 568, 234, 87, 45, 69, 423, 867]
print(type(a))
a.append(56)
print(a)

c = []
for num in a:
    if num % 2 != 0:
        c.append(num)
    if num % 2 == 0:
        c.insert(0, num)
print("new list ", c)

num = "1223343"
jump = False
for i in range(1, len(num)-1):
    print("wew", i, num[i])
    if int(num[i]) == (int(num[i - 1]) + 1) or int(num[i]) == (int(num[i - 1]) - 1):
        jump = True
    else:
        jump=False
    if int(num[i]) == (int(num[i + 1]) - 1) or int(num[i]) == (int(num[i + 1]) - 1):
        jump = True
    else:
        jump = False
print(jump)
