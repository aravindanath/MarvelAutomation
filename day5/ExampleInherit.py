
# parent
class Cars():

    def wheels(self,no):
        print("Wheels " ,no)


    def colour(self, col):
        print("Car colour is ",col)

class ThreeM(Cars):

    def winSheeld(self):
        print("Wiper")

#child
class BMW(ThreeM):

    def bmwWheels(self):
        BMW.wheels(self,4)


b = BMW()

b.wheels(6)
b.bmwWheels()
b.colour("MBlue")
b.winSheeld()