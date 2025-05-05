# 10. Instance Methods

class Dog:
  def __init__(self, name: str, breed: str) -> str:
    self.name = name
    self.breed = breed

  def bark(self):
    print(f"{self.name} is Barking.")

dog1 = Dog("Buddy", "Labrador")
dog1.bark()