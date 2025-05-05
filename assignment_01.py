# assignment-1

class Student:
  def __init__(self, name: str, marks:float):
    self.name = name 
    self.marks = marks

  def display(self):
    print(f"Student Name: {self.name}\nStudent Marks: {self.marks}")

std1 = Student("Rani", 25)
std2 = Student("Ashraf", 35)
std1.display()
std2.display()