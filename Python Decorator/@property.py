#@property decorator used to define a method as a property and it can be assessed like an attribute

class Marvel:
    def __init__(self,averagers, xmen):
        self._averagers=averagers
        self._xmen=xmen
        self.avengers_list=["Ant-man","Captain Marvel","Wasp","Hulk","Thor Odinson","Black Panther","Vision","Ironman","Balck Widow"]
    @property
    def averagers(self):
        return f"avergers are {self._averagers}"
    @property
    def xmen(self):
        return f"xmen are {self._xmen}"
    
    @averagers.setter
    def averagers(self,new_averagers):
        if new_averagers not in self.avengers_list:
            print(f"Heros are no existing in the {self.avengers_list}")
        else:
            self.averagers=new_averagers
    @averagers.deleter
    def averagers(self):
        del self._averagers
        print(f"{self.averagers} has been deleted")



a=Marvel("Captain Marvel","Maneto")
print(a._averagers,a._xmen)
print(a.averagers)
a.averagers="Superman"
print("setter method", a.averagers)
del a.averagers







# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#                        Benefit: Add additional logic when you read, write, or delete attributes
#                        Gives you a getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3, 4)