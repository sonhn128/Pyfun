class People:
    def __init__(self,eyeColor, hairColor, skinColor):
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.skinColor = skinColor
class European(People):
    def __init__(self,country):
        People.__init__(self,'blue','white','blond')
        self.country = country
    def goodAtSport(self):
        print("%s good at sport"% self.country)
    def __str__(self):
        return "%s person has %s eye, %s skin, %s hair"%(self.country, self.eyeColor,self.hairColor,self.skinColor)

class Asian(People):
    def __init__(self,country):
        People.__init__(self,'black','yellow','black')
        self.country = country
    def goodAtMath(self):
        print("%s good at math"% self.country)
    def __str__(self):
        return "%s person has %s eye, %s skin, %s hair"%(self.country, self.eyeColor,self.hairColor,self.skinColor)
Japanese = Asian('Japanese')
French = European('French')
print(French)
print(Japanese)