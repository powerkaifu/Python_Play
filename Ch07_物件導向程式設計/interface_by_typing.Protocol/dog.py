# 實作不需要繼承任何類別，只需要實作 Protocol 定義的方法
class Dog:

  def make_sound(self) -> str:
    return "Bark"

  def move(self) -> str:
    return "Run"
