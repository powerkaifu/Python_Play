# 使用 ABC 來定義介面
from abc import ABC, abstractmethod


# 定義介面
class Animal(ABC):

  @abstractmethod
  def make_sound(self) -> str:
    pass

  @abstractmethod
  def move(self) -> str:
    pass
