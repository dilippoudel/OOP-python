# TV Class
class TV:
    def __init__(self, brand, location):
        self.brand = brand,
        self.location = location,
        self.isOn = False
        self.isMuted = False
        self.channelList = [2, 11, 9, 12, 22, 27, 29, 33, 57]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM

    def power(self):
        self.isOn = not self.isOn  # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channel_up(self):
        if not self.isOn:
            return
        self.channelIndex += 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0

    def channel_down(self):
        if not self.isOn:
            return
        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def set_channel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)

    def showInfo(self):
        print()
        print('TV STATUS')
        if self.isOn:
            print(f'    TV is : On\n'
                  f'    TV is in: {self.location}\n'
                  f'    Brand: {self.brand}\n'
                  f'    Channel is: {self.channelList[self.channelIndex]}')
            if self.isMuted:
                print(f'    Volume is {self.volume}. Sound is Muted.')
            else:
                print(f'    Volume is {self.volume}')
        else:
            print(f'    TV is: OFF')


otv = TV('Samsung', 'Bedroom')
otv.power()
otv.showInfo()
otv.channel_up()
otv.showInfo()
otv.mute()
otv.set_channel(22)
otv.showInfo()
otv.power()
print(otv.location)
otv.showInfo()