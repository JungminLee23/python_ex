class TV:
    """
    power, volume, size 프로퍼티를 가진 클래스
    생성자를 통해 초기화
    switch() : power의 on / off를 담당
    set_volume() : volume 조절
    watch() : power 여부에 따라 on 상태면 tv 보는 중...
              off 상태면 tv를 켜세요 베세지 보여주기
    """

    def __init__(self, power, volume, size):
        self.power = power
        self.volume = volume
        self.size = size

    def switch(self):
        self.power = not (self.power)

    def set_volume(self, volume):
        self.volume = volume

    def watch(self):
        # if self.power:
        #     print("tv 보는 중...")
        # else:
        #     print("tv를 켜세요")
        str = "TV보는 중" if self.power else "tv를 켜세요"
        return str


user1 = TV(False, 10, 20)
print(user1.watch())
user1.switch()
print(user1.watch())
print(user1.volume)
user1.set_volume(20)
print(user1.volume)
