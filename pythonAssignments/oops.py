class food:
    requirement = "survival"
    def __init__(self,type,fanBase):
        self.type=type
        self.fanBase=fanBase

biriyani=food("Non veg",10.0)
rice=food("Veg", 9)

print("Biriyani is a ",biriyani.type," dish, with a fan base rating of ", biriyani.fanBase)
print("Rice is a ",rice.type," dish, with a fan base rating of ", rice.fanBase)
print("Both of them are required for ", food.requirement)