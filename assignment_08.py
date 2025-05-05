# 8. The super() Function

class Person:
  def __init__(self, name: str) -> str:
    self.name = name

class Teacher(Person):
  def __init__(self, name: str, subject: str) -> str:
    super().__init__(name)
    self.subject = subject

teacher1 = Teacher("Rani", "Python")
print(f"Name: {teacher1.name}")
print(f"Subject: {teacher1.subject}")