class Shape(object):
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # getter - getting value of real attribute
    @property
    def width(self):
        return self.__width

    # getter - getting value of real attribute
    @property
    def height(self):
        return self.__height

    # setter - setting real attribute to assigned value of fake property
    @width.setter
    def width(self, v):
        self.__width = v

    # setter - setting real attribute to assigned value of fake property
    @height.setter
    def height(self, v):
        self.__height = v

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        # This does not require self?
        super().__init__(width, height)
        # This does require self...?
        # Shape.__init__(self, width, height)


    # getter - getting value for a fake property
    @property
    def area(self):
        return self.width * self.height

    # getter - getting value for a fake property
    @property
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    # getting the stats for all attributes and properties in a readable format
    def getStats(self):
        return """width:     {}
height:    {}
area:      {}
perimeter: {}""".format(self.width, self.height, self.area, self.perimeter)


def main():
    print("Rectangle a:")
    a = Rectangle(5, 7)
    print("area:      {}".format(a.area))
    print("perimeter: {}".format(a.perimeter))

    print("")
    print("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    print(b.getStats())


if __name__ == '__main__':
    main()
