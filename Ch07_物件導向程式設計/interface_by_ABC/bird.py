from animal import Animal


class Bird(Animal):

  def make_sound(self) -> str:
    return "Chirp"

  def move(self) -> str:
    return "Fly"
