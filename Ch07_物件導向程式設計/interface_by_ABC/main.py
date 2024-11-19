from animal import Animal
from dog import Dog
from bird import Bird

john = Dog()
mary = Bird()


def animal_action(animail: Animal):
  print(animail.make_sound())
  print(animail.move())


animal_action(john)
animal_action(mary)
