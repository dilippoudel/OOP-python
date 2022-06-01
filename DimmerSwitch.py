class DimmerSwitch:
    def __init__(self, label, age, brand):
        self.isSwitchOn = False
        self.current_range = 0
        self.label = label
        self.age = age
        self.brand = brand

    def turn_on(self):
        self.isSwitchOn = True
        self.current_range = 1

    def turn_off(self):
        self.isSwitchOn = False
        self.current_range = 0

    def raise_brightness_level(self):
        if self.current_range < 10:
            self.isSwitchOn = True
            self.current_range += 1
        else:
            self.isSwitchOn = True
            self.current_range = 10

    def lower_brightness_level(self):
        if self.current_range > 0:
            self.isSwitchOn = True
            self.current_range -= 1
        else:
            self.current_range = 0
            self.isSwitchOn = False

    def show(self):
        print()
        print(self.isSwitchOn)
        print(self.current_range)




