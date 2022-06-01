class SwitchLight:
    def __init__(self):
        self.IsSwitchOn = False

    def turn_on(self):
        self.IsSwitchOn = True

    def turn_off(self):
        self.IsSwitchOn = False

    def show(self):
        print(self.IsSwitchOn)


oLightOn = SwitchLight()
oLightOn.show()
oLightOn.turn_on()
oLightOn.show()
oLightOn.turn_off()
oLightOn.show()
print(type(oLightOn))
