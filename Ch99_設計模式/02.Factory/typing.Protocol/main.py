from factory.archer_training_camp import ArcherTrainingCamp
from factory.warrior_training_camp import WarriorTrainingCamp

archer_camp = ArcherTrainingCamp()
warrior_camp = WarriorTrainingCamp()

archer = archer_camp.train_adventurer()
warrior = warrior_camp.train_adventurer()

print(archer.fight())  # 輸出：Archer fights with a bow and arrow.
print(warrior.fight())  # 輸出：Warrior fights with a sword and shield.
