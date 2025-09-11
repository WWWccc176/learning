class MobilePhone:
    def __init__(self, brand, theType):
        self.brand = brand
        self.theType = theType

    def print_brand_type(self):
        print(f"{self.brand} {self.theType}")

mobile_phone_a = MobilePhone("iPhone", "13")

mobile_phone_a.print_brand_type() 