# Interface Segregation Principle
# suggests that a class should not be forced to implement methods it doesn't need. In other words, 
# a class should have small, focused interfaces rather than large, monolithic ones.

# for example here we have a class makeing shapes.

from abc import ABC, abstractmethod

class ShapeInterface(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod    
    def calculate_volume(self):
        pass

# if i want to define a class to make a square i dont need to calcute volume for square
class Square(ShapeInterface):

    def calculate_area(self):
        pass

    def calculate_volume(self):
        pass
        # calculate volume
        # not using here!!!

# to fix that problem we should seprate 3D shapes class

# FIXING BY ISP

from abc import ABC, abstractmethod

class ShapeInterface(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class ThreeDimensionalShapeInterface(ShapeInterface):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_volume(self):
        pass

# now we can make 2D and 3D shapes sepratly by using ISP 
class Square(ShapeInterface):

    def calculate_area(self):
        # calculate area
        pass

class Cuboid(ThreeDimensionalShapeInterface):

    def calculate_area(self):
        # calculate area 
        pass

    def calculate_volume(self):
        # calculate volume
        pass

class Rectangle(ShapeInterface):
    
    def calculate_area(self):
       # calculate area
       pass