class Car:
    """
    Car class
    Author : Lee
    Date : 2020.08.13
    Description : Class 작성법 /생성자
    """

    car_count = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        Car.car_count += 1

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

    def __del__(self):
        Car.car_count -= 1


# 객체 생성
myCar1 = Car("Red", 10)
myCar2 = Car("Blue", 20)
myCar3 = Car("Green", 30)

print("생산된 총 자동차 수 : {}".format(Car.car_count))
