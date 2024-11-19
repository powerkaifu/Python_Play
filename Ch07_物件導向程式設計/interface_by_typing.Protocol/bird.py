# 實作不需要繼承任何類別，只需要實作 Protocol 定義的方法
class Bird:

  def make_sound(self) -> str:
    return 'Chirp'

  def move(self) -> str:
    return 'Fly'
