# 14. Aggregation

class Department:
  def __init__(self, name: str) -> None:
    self.name = name

class Employee:
  def __init__(self, name: str, department: Department) -> None:
    self.name = name
    self.department = department

department = Department("IT")
employee = Employee("John", department)

print(employee.department.name)