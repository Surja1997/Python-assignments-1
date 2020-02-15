def binary(n, s=""):
    if n == 1 or n == 0:
        s = str(n) + s
        return s
    else:
        s = str(n % 2) + s
        n = int(n / 2)
        return binary(n, s)


n = int(input("number"))
k=binary(n, "")
splitted=k.split("0")
splitted.sort()
print(len(splitted[len(splitted)-1]))
