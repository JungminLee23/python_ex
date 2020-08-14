import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius
        # 언더바 두개가 붙으면 __이름 --> private 형으로 선언된다.
        # 즉, 외부에서 접근 불가

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_circleArea(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        self.__radius = value


circle = Circle(20)
print("원의 둘레", circle.get_circumference())
print("원의 면적", circle.get_circleArea())


print()
circle.set_radius(10)
print("원의 둘레", circle.get_circumference())
print("원의 면적", circle.get_circleArea())
# print(circle.__radius)  # private이기 때문에 이게 에러가 난다.
print(circle.get_radius())

