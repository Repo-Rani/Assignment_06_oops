# 5. Static Variables and Static Methods

class MathUtils:
  @staticmethod
  def sum_numbers(a:int, b:int) -> int :
    return a + b
  
result = MathUtils.sum_numbers(6, 8)
print(f"Sum of your numbers are: {result}")