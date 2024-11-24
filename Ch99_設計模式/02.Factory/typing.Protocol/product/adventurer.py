from typing import Protocol


class Adventurer(Protocol):

  def fight(self) -> str:
    pass
