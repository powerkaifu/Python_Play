from abc import ABC, abstractmethod


# 由於 Python 沒有 interface 關鍵字，所以使用 ABC 來定義介面
class Adventurer(ABC):

  @abstractmethod
  def fight(self) -> str:
    pass


# 實現 Adventurer 介面
class Archer(Adventurer):

  def fight(self) -> str:
    return "Archer fights with a bow and arrow."


# 實現 Adventurer 介面
class Warrior(Adventurer):

  def fight(self) -> str:
    return "Warrior fights with a sword and shield."


class TrainingCamp:

  @staticmethod
  def train_adventurer(type):
    if type == 'archer':
      return Archer()
    elif type == 'warrior':
      return Warrior()
    else:
      raise ValueError('Type not supported.')


archer = TrainingCamp.train_adventurer('archer')
warrior = TrainingCamp.train_adventurer('warrior')

print(archer.fight())  # 輸出：Archer fights with a bow and arrow.
print(warrior.fight())  # 輸出：Warrior fights with a sword and shield.
