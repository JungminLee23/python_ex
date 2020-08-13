class UserInfo:
    """
    클래스 작성 시 클래스에 관한 정보 넣기(권고 사항)
    UserInfo class / 인자있는 생성자 만들기
    Author : Park
    Date : 2020.08.12
    Description : Class 작성법
    """

    # 생성자 : 생성자 오버로딩 개념 없음
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 따로 인스턴스 변수 선언을 하지 않고 여기서 이렇게 해도
        # 인스턴스 변수로 인식 됨

    # Instance Method : self를 인자로 가지고 있어야 함
    def user_info(self):
        print("메소드 실행")

    def __str__(self):
        return "name : {}, age : {}".format(self.name, self.age)


# 객체 생성
user1 = UserInfo("홍길동", 25)
user2 = UserInfo("홍홍홍", 24)
# 메소드 호출
# user1.user_info()
print(user1)
print(user2.__dict__)
