from abc import ABC, abstractmethod


# 產品介面
class Adventurer(ABC):

  @abstractmethod  # 定義抽象方法
  def fight(self) -> str:
    pass
