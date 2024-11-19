from animal import Animal  # 這是一個介面
from dog import Dog
from bird import Bird

john = Dog()
mary = Bird()


# 使用介面
def animal_action(animail: Animal):
  print(animail.make_sound())
  print(animail.move())


animal_action(john)
animal_action(mary)
