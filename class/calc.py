class Calculator:
    """
    Calculator Class
    Author : ..
    Date : 2020.08.13
    Description : Class 생성
    """

    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print("cal1 : {}".format(cal1.adder(10)))
print("cal2 : {}".format(cal2.adder(1.0)))
