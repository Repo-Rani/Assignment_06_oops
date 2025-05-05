# 17. Class Decorators

class add_greeting:
  def __init__(self, cls):
    self.cls = cls

  def __call__(self, *args, **kwargs):
    instance = self.cls(*args, **kwargs) 
    instance.greet = lambda: "Hello from Decorator!"
    return instance

@add_greeting
class Person:
  def __init__(self, name):
    self.name = name

p = Person("Alice")
print(p.greet())