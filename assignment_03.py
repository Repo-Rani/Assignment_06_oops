# 3. Public Variables and Methods

class Car:
  def __init__(self, brand: str):
    self.brand = brand

  def start(self):
    print("Car is Starting...")

car1 = Car("XYZ")
print(car1.brand)
car1.start()