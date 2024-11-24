# 單例模式計算器
class Calculator:
  __instance = None

  #  *args 用於將不定數量的位置參數傳遞給函數
  # **kwargs 用於將不定數量的關鍵字參數傳遞給函數
  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    return cls.__instance

  def add(self, a, b):
    return a + b

  def subtract(self, a, b):
    return a - b

  def multiply(self, a, b):
    return a * b

  def divide(self, a, b):
    if b == 0:
      raise ValueError("Cannot divide by zero")
    return a / b


# 測試單例模式計算器
calculator1 = Calculator()
calculator2 = Calculator()

print(calculator1 is calculator2)  # True

# 使用計算器進行加減乘除運算
print(calculator1.add(10, 5))  # 15
print(calculator1.subtract(10, 5))  # 5
print(calculator1.multiply(10, 5))  # 50
print(calculator1.divide(10, 5))  # 2.0
