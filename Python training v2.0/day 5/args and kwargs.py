def kwargs_demo(**kwargs):
    print(type(kwargs))
    for key, val in kwargs.items():
        print(key, "=>", val)


kwargs_demo(Sachin=55, Virat=['one', 'two', 'three'], Rohit=44)
