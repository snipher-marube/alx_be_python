import math

class Shape:
    """Base class representing a geometric shape."""
    
    def area(self):
        """Calculate the area of the shape.
        
        Raises:
            NotImplementedError: This method should be overridden by subclasses
        """
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            float: The area (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    
    def __init__(self, radius):
        """Initialize a circle with radius."""
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: The area (π × radius²)
        """
        return math.pi * (self.radius ** 2)