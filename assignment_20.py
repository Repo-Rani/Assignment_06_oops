# 20. Creating a Custom Exception

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Age {age} is invalid. Must be 18 or older."
        super().__init__(self.message) 
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is valid.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")  