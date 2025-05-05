# 9. Abstract Classes and Methods

from abc import ABC, abstractmethod
class Shape(ABC):
  @abstractmethod
  def area(self):
    pass

class Rectangle(Shape):
  def __init__(self, length: float, width: float) -> float:
    self.length = length
    self.width = width

  def area(self) -> float:
    return self.length * self.width
  
rec1 = Rectangle(2, 3)
print(f"Area of Rectangle: {rec1.area()}")