class Audio:
    """
    power, volume을 가진 클래스
    power => True, False
    volume => 정수

    switch() => power 값을 변경
    turn() => power 켜져있으면 음악 재생 
              꺼져있으면 power 켜라는 메시지 출력
    volume() => volume 값을 변경
    """

    def __init__(self, power, vol):
        self.power = power
        self.vol = vol

    def switch(self):
        self.power = not (self.power)

    def turn(self):
        if self.power:
            print("음악 재생")
        else:
            print("power 켜야 함")

    def volume(self, vol):
        self.vol = vol


# 파이썬 삼항 연산자 개념

# 자바 :
# 조건 ? 참 : 거짓

#  파이썬 :
# (참일 때 실행 될 구문) if (조건) else (거짓일 때 실행 될 구문)
# --> 참 if 조건 else 거짓
mp3 = Audio(False, 9)
mp3.volume(12)
mp3.turn()
mp3.switch()
mp3.turn()
