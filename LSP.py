'''
The Liskov Substitution Principle states that objects of a superclass should be 
replaceable with objects of a subclass without affecting the functionality of the program. 
Essentially, derived classes must be substitutable for their base classes.

A very common example is the rectangle-square scenario. It is clear that all squares are rectangles
because they are quadrilaterals with all four angles being right angles. However, not every rectangle
is a square. To be a square, the length of its sides must be the same.
With this in mind, suppose you have a rectangle class to calculate the area of a rectangle and 
perform other operations like setting the color:
'''

class Rectangle:

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_color(self, color):
        pass

    def get_area(self):
        return self.width * self.height
    
'''
Knowing that all squares are rectangles, you can inherit the properties of a rectangle. 
Since the width and height must be the same, you can set it up like this:
'''

class Square(Rectangle):

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.width = height 
    self.height = height


# In the above example, you'll notice that a rectangle is created and the width and height are set.
# Then, you can calculate the correct area.

rectangle = Rectangle()
rectangle.set_width(10)
rectangle.set_height(5)
print(rectangle.get_area())  # 50

# However, according to the LSP, you want your subclass objects to behave like your superclass objects.
# This means that if you replace the rectangle with a square, everything should work fine:

square = Square()
square.set_width(10)
square.set_height(5)

# You should get 100 because setWidth(10) is supposed to set both the width and height to 10.
# But due to setHeight(5), this value returns 25.

square = Square()
square.set_width(10)
square.set_height(5)
print(square.get_area())  # 25

# This breaks the LSP. To fix this issue, you should have a general class for all shapes that contains 
# all the common methods you want your subclass objects to access. Then, for individual methods, 
# you create separate classes for Rectangle and Square.

class Shape:

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class Rectangle(Shape):

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Shape):

    def set_side(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

# This way, you can set and get the color using the superclass or subclass:

# superclass
shape = Shape()
shape.set_color('red')
print(shape.get_color())  # red

# subclass
rectangle = Rectangle()
rectangle.set_color('red')
print(rectangle.get_color())  # red

# subclass
square = Square()
square.set_color('red')
print(square.get_color())  # red

