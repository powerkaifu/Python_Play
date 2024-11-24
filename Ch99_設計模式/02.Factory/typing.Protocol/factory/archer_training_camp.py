from product.adventurer import Adventurer
from product.archer import Archer
from factory.training_camp import TrainingCamp


class ArcherTrainingCamp(TrainingCamp):

  def train_adventurer(self) -> Adventurer:
    return Archer()
