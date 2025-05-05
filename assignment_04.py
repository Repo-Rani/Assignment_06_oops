# 4. Class Variables and Class Methods

class Bank:
    bank_name: str = "Bank Al Habib"

    def __init__(self, account_holder: str):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name: str):
        cls.bank_name = name

b1 = Bank("Rani")
b2 = Bank("Ashraf Ali")

print(f"Bank name for b1 before change: {b1.bank_name}")
print(f"Bank name for b2 before change: {b2.bank_name}")

Bank.change_bank_name("Habib Bank Limited")

print(f"Bank name for b1 after change: {b1.bank_name}")
print(f"Bank name for b2 after change: {b2.bank_name}")
print(f"Current bank name (accessed directly from class): {Bank.bank_name}")