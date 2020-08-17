class FourCal:
    def __init__(self):
        super().__init__()

    def sum(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 // num2


if __name__ == "__main__":
    test = FourCal()
    print(test.sum(5, 4))
    print(test.sub(4, 2))
    print(test.mul(2, 4))
    print(test.div(4, 2))

