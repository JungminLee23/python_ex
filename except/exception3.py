# 사용자 정의 예외

# Exception을 상속받아서 나만의 Exception을 만드는 것
class CustomException(Exception):
    def __init__(self):
        super().__init__(self)
        print("사용자 정의 예외")

    def __str__(self):
        return "오류 발생"


raise CustomException

