class Account:
    """
    은행계좌 클래스
    계좌번호, 이름, 잔액을 받아서 객체 생성
    입금 / 출금 기능의 메소드 구현
    """

    def __init__(self, accountNum, name, money):
        self.accountNum = accountNum
        self.name = name
        self.money = money

    def input_money(self, money):
        self.money += money

    def output_money(self, money):
        self.money -= money

    def __str__(self):
        return "{} : 잔액 {}".format(self.name, self.money)


user1 = Account("1111", "he", 10000)
user2 = Account("2222", "sung", 20000)

user1.input_money(20000)
print(user1.money)
user1.output_money(10000)
print(user1)

user2.input_money(100000)
user2.output_money(20000)
print(user2)
