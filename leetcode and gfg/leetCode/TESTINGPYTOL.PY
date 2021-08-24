class parent : 
    def __init__(self, name) : 
        self.name = name
    def showName(self): 
        print(self.name)
    def somthing (self):
        print('its a parent class')

    
    @classmethod
    def sayhi(cls):
        print("hi")

class child (parent) : 
    def theX(self, x): 
        self.x = x
    def printX(self):
        print(self.x)
        super().somthing()
        parent.sayhi()
        parent.somthing(self)

p = parent('neels')
p.showName()
print(f"\nname: {p.name} \n")
c= child('sandeep')
c.showName()
c.theX(28)
c.x = 'hello'
c.printX()

parent.sayhi()
print(c)
print(type(c))

c.printX()



# class std: 
#     pass

# student1 = std()
# student1.name = "neels"

# print(student1.name)


    