class SelfTest:
    @classmethod
    def function1(cls):
        print("function1() called")

    def function2(self):
        print("function2() called")


self_test = SelfTest()

# 클래스 메소드 호출하는 방법
self_test.function1()
SelfTest.function1()
# 인스턴스 메소드 호출하는 방법
self_test.function2()
SelfTest.function2(self_test)
#  SelfTest.function2() - 안됨

