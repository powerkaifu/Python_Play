from product.adventurer import Adventurer
from product.warrior import Warrior
from factory.training_camp import TrainingCamp


class WarriorTrainingCamp(TrainingCamp):

  def train_adventurer(self) -> Adventurer:
    return Warrior()
