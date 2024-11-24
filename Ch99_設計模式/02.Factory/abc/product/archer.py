from .adventurer import Adventurer


# 具體產品，實作 Adventurer 介面
class Archer(Adventurer):

  def fight(self) -> str:
    return "Archer fights with a bow and arrow."
