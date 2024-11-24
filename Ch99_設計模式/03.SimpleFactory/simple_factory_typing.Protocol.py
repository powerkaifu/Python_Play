from typing import Protocol


# 定義 Adventurer 協議
class Adventurer(Protocol):

  def fight(self) -> str:
    pass


# 定義 Archer 類，實作 Adventurer 協議
class Archer:

  def fight(self) -> str:
    return "Archer fights with a bow and arrow."


# 定義 Warrior 類，實作 Adventurer 協議
class Warrior:

  def fight(self) -> str:
    return "Warrior fights with a sword and shield."


# 定義 TrainingCamp 工廠
class TrainingCamp:

  @staticmethod
  def train_adventurer(adventurer_type: str) -> Adventurer:
    if adventurer_type == 'archer':
      return Archer()
    elif adventurer_type == 'warrior':
      return Warrior()
    else:
      raise ValueError("Unknown adventurer type")


# 測試簡單工廠模式

archer = TrainingCamp.train_adventurer('archer')
warrior = TrainingCamp.train_adventurer('warrior')

print(archer.fight())  # 輸出：Archer fights with a bow and arrow.
print(warrior.fight())  # 輸出：Warrior fights with a sword and shield.
