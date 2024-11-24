from product.adventurer import Adventurer


# 具體產品，實作 Adventurer 介面
class Warrior(Adventurer):
  # 實作抽象方法
  def fight(self) -> str:
    return "Warrior fights with a sword and shield."
