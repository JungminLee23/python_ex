class UserInfo:
    """
    클래스 작성 시 클래스에 관한 정보 넣기(권고 사항)
    UserInfo class
    Author : Park
    Date : 2020.08.12
    Description : Class 작성법
    """

    # Instance Method : self를 인자로 가지고 있어야 함
    def user_info(self):
        print("메소드 실행")


# 객체 생성
user1 = UserInfo()

# 메소드 호출
user1.user_info()
