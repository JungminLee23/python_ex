class UserInfo:
    """
    클래스 작성 시 클래스에 관한 정보 넣기(권고 사항)
    UserInfo class
    Author : Park
    Date : 2020.08.12
    Description : Class 작성법
    """

    # 생성자 : 생성자 오버로딩 개념 없음
    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email
        # 이메일이 필수 요소가 아닐 경우

    # Instance Method : self를 인자로 가지고 있어야 함
    def user_info(self):
        print("메소드 실행")

    def __str__(self):
        return "name : {}, age : {}, email : {}".format(self.name, self.age, self.email)


# 객체 생성
user1 = UserInfo("홍길동", 25)
user2 = UserInfo("성춘향", 24, "sung5@google.com")

# 메소드 호출
# user1.user_info()

print(user1)
print(user2)

