class AudioVisual:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

    def switch(self, on_off):
        self.power = on_off

    def set_volume(self, vol):
        self.volume = vol


class Audio(AudioVisual):
    def __init__(self, power, volume):
        super().__init__(power, volume)

    def turn(self):
        if self.power:
            print("음악 재생")
        else:
            print("power 켜야 함")


class TV(AudioVisual):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size

    def watch(self):
        # if self.power:
        #     print("tv 보는 중...")
        # else:
        #     print("tv를 켜세요")
        str = "TV보는 중" if self.power else "tv를 켜세요"
        print(str)


tv = TV(False, 12, 48)
tv.switch(True)
tv.watch()

audio = Audio(True, 15)
audio.set_volume(20)
audio.turn()
