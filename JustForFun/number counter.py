c=0
for i in range(11,101):
    num=str(i)
    if '6' in num:
        c+=num.count('6')
print(c)