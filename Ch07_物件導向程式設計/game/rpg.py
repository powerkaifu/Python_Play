# 父類別 - 讓子類別繼承共同屬性、方法
class Role:

  def __init__(self, name: str, level: int, blood: int) -> None:
    self.name = name
    self.level = level
    self.blood = blood

  def __str__(self):
    return f'({self.name!r}, {self.level}, {self.blood})'

  def __repr__(self):
    return self.__str__()


# 子類別 - 繼承父類別的屬性、方法，並新增自己的方法
class SwordsMan(Role):

  def fight(self):
    print('揮劍攻擊')

  def __str__(self):
    return f'強壯無敵的 {super().__str__()}'


class Magician(Role):

  def fight(self):
    print('魔法攻擊')

  def cure(self):
    print('魔法治療')

  def __str__(self):
    return f'具有破壞力的 {super().__str__()}'


class Duck:
  pass
