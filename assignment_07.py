# 7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name: str, salary: int, ssn: str):
        self.name = name         # Public variable: Accessible from anywhere.
        self._salary = salary     # Protected variable: Convention to not access directly from outside the class.
        self.__ssn = ssn         # Private variable: Name-mangled to make direct access from outside difficult.

emp1 = Employee("Rani", 600000, "768456857")

# Accessing the public variable:
print(f"Accessing public variable 'name': {emp1.name}")

# Accessing the protected variable:
print(f"Accessing protected variable '_salary': {emp1._salary}")
# Note: While you can access protected members directly, it's generally considered bad practice.

# Attempting to access the private variable directly:
try:
    print(f"Accessing private variable '__ssn': {emp1.__ssn}")
except AttributeError as e:
    print(f"Error accessing private variable '__ssn__': {e}")
    print("Private variables with double underscore prefix are name-mangled by Python.")
    print("They are intended for internal use within the class.")

# Accessing the private variable using its mangled name (generally not recommended):
print(f"Accessing private variable '__ssn' using mangled name '_Employee__ssn': {emp1._Employee__ssn}")
# Note: Accessing private members using name mangling should generally be avoided
# as it breaks the encapsulation intended by the private modifier.