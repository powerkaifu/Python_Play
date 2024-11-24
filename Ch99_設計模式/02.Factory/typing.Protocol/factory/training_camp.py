from typing import Protocol
from product.adventurer import Adventurer


class TrainingCamp(Protocol):

  def train_adventurer(self) -> Adventurer:
    pass
