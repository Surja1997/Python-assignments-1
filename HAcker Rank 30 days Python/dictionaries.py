# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
try:
    n = int(input())
    address_book = dict()
    for i in range(n):
        name_phone = str(input())
        split = re.split(" ", name_phone)
        address_book[split[0]] = split[1]
    queries = str(input())
    while queries is not None:
        if queries in address_book:
            print(queries,end="=")
            print(address_book[queries])
        else:
            print("Not found")
        queries = str(input())
except EOFError as e:
    print()


