class Property_Setter:
    temp = 100

    @property
    def what_temp(self):
        return Property_Setter.temp

    @what_temp.setter
    def what_temp(self, value):
        Property_Setter.temp = value

ps1 = Property_Setter()
ps1.temp
ps1.what_temp
ps1.what_temp = 200
ps1.what_temp
ps1.temp
