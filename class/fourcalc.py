class FourCal:
    """
    FourCal
    사칙연산 기능을 가지고 있는 계산기
    두 개의 정수를 받아 사칙 연산을 한 후 연산 결과를 리턴하는
    4개의 메소드를 작성한다.
    생성자는 두 개의 변수를 초기화하는 형태로 작성한다.
    """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


test1 = FourCal(10, 20)

print(test1.sum())
print(test1.minus())
print(test1.mul())
print(test1.div())
