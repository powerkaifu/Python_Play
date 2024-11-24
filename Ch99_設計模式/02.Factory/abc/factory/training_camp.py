from abc import ABC, abstractmethod
from product.adventurer import Adventurer


class TrainingCamp(ABC):

  @abstractmethod
  def train_adventurer(self) -> Adventurer:
    pass
