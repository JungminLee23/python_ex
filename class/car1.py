class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


# 객체 생성
myCar1 = Car()
myCar1.speed = 0
myCar1.color = "Red"

myCar2 = Car()
myCar2.speed = 20
myCar2.color = "Blue"

myCar3 = Car()
myCar3.speed = 30
myCar3.color = "Yellow"

myCar1.upSpeed(20)
print("자동차1의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar1.color, myCar1.speed))

myCar2.upSpeed(70)
print("자동차2의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar2.color, myCar2.speed))

myCar3.upSpeed(150)
print("자동차3의 색상은 {} 이며, 현재 속도는 {:3d}km".format(myCar3.color, myCar3.speed))
