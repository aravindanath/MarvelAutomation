
"""
class
methods
constructs / special methods
@classmethod
@Staticmethod

"""


class Methods():
    # Global varibale

    city = "Bangalore"

    def __init__(self):
        print("i am a constructor")

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("i am a constructor")

    def normalMethod(self):
        print("I am a normal method")
        print(self.city)


    def expVarible(self):
        print("My name is ",self.name)
        print("My age is ",self.age)


    def parm1(self,a):
        print("Single parm", a)

    def parmMultiValues(self, *args):
        print(type(args)," ---->  multiple parm", args)


    def parmMulitiKeyvale(self, **kwargs):
        print(type(kwargs), " ---->  multiple parm", kwargs)

    @classmethod
    def demoClsMethod(cls):
        print(cls.city)

    @staticmethod
    def demoStatMethod():

        print("I am static method")




# Object of the class
m = Methods("arvind",30)
m.normalMethod()
m.expVarible()
m.parm1("Vijaya")
m.parmMultiValues("Vijaya","Sridhar","raj","Mitali","arpita","siram")
m.parmMulitiKeyvale(name="arvind",age="30",hobby="reading")
m.demoClsMethod()


Methods.demoStatMethod()