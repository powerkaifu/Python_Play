from animal import Animal


# 實作介面(但是是用繼承的方式)
## 這是因為 Python 並沒有介面(interface)的機制，只能透過繼承的方式來實作介面
class Dog(Animal):

  def make_sound(self) -> str:
    return 'Bark'

  def move(self) -> str:
    return 'Run'
