# 6. Constructors and Destructors

class Logger:
  def __init__(self, name: str):
    self.name = name
    print(f"Hey {self.name}, You've successfully Logged in!")

  def __del__(self):
    print(f"Ops, You Logged out!")

user1 = Logger("Rani")
user2 = Logger("Ashraf")

del user1
del user2