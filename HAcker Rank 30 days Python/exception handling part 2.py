# Write your code here
class Calculator:
    def power(n, p):
        if n < 0 or p < 0:
            return Exception
        else:
            return n ** p


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    print(n,"dd",p)
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
