
class TemperatureConverter:
  @staticmethod
  def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32
  
print(TemperatureConverter.celsius_to_fahrenheit(30))