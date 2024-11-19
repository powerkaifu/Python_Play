# 使用 typing.Protocol 定義介面
## 這種方法更符合 Python 的鴨子型別哲學，只要它走路像鴨子、叫聲像鴨子，那它就是鴨子
from typing import Protocol


# 定義介面
class Animal(Protocol):

  # -> str 只是為了讓方法表達更清楚，並不是強制的，即便回傳型別不是 str 也不會報錯
  def make_sound(self) -> str:
    pass

  def move(self) -> str:
    pass
