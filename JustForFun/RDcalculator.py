t = int(input('Enter the number of years'))
p = int(input('Enter the amount per year'))
r = float(input('Enter interest PA'))
n = int(input('Enter the number of times compounded in a year'))
amount = 0.0
comp_total = 0
original_P = p


def amt(principal, rate, time, ann_freq):
    if time == 10:
        amount = principal * 2

    else:
        amount = principal * ((1 + (rate / (ann_freq * 100))) ** (time * ann_freq))
    return amount


for i in range(0, t):
    A = amt(p, r, 1, n)
    p = A + original_P
net_invested: int = original_P * t
print('amount invested = ', net_invested)
print('amount you will receive', p)
print('percent increase = ', (p - net_invested) / (net_invested) * 100)
