class Human():
    def __init__(self, name, age):
        self.name = name  # name is public
        self.__age = age  # __age is private

    def who(self):
        return self.name

    def how_old(self):
        return self.__age


class Police(Human):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

    def PK(self):
        if self.power > 50:
            return True
        else:
            return False


if __name__ == '__main__':
    clay = Police('Clay', 25, 70)
    print('Name:', clay.who())
    print('Age:', clay.how_old())
    print('PK:', clay.PK())
