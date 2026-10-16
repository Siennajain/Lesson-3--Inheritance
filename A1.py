class parent:

    def __init__(self,height,eyecolour):
        self.eyecolour=eyecolour
        self.height=height

    def showtraits(self):
        print("Eye colour: ", self.eyecolour)
        print("Height: ", self.height)

class kid(parent):

    def __init__(self, name, age, height, eyecolour):
        self.name=name
        self.age=age
        super().__init__(height, eyecolour)

    def showtraits(self):
        print("Name:",self.name)
        print("Age:", self.age)
        super().showtraits()

    def hobby(self,hobby):
        print(self.name,"'s Favourite Hobby:",hobby)

obj=parent(150,"blue")
obj.showtraits()
child=kid("Sienna",14, 140,"brown")
child.showtraits()
child.hobby("singing")

print("Is kid child class of parent class?\n",issubclass(kid,parent))

