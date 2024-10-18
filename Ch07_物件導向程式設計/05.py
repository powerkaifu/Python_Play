'''
學號：511171017
姓名：張凱富
'''

import math


# 定義類別
class shape:

  # 初始化，self 指的是物件(實例)本身
  def __init__(self, r):
    self.rad = r

  # 每個方法的第一個參數必須是 self
  # 回傳體積
  def volume(self):
    return (4 / 3) * math.pi * self.rad**3

  # 回傳表面積
  def surface_area(self):
    return 4 * math.pi * self.rad**2

  # (a)查詢物件時，定義表示的字串
  def __repr__(self):
    return f'Sphere object, rad = {self.rad}'

  # (b)
  def __str__(self):
    return f'Sphere object, rad = {self.rad},volume = {self.volume():.2f},surface area = {self.surface_area():.2f}'


# 建立一個半徑為 2 的球體
s0 = shape(2)
s0_volume = s0.volume()
s0_surface = s0.surface_area()

# 小數點取到第二位
print(f's0 的體積: {s0_volume:.2f}，表面積: {s0_surface:.2f}')

# (a) 使用 repr 函式查詢 s0，會呼叫 __repr__ 方法
print(repr(s0))

# (b) 查詢 s0，會呼叫 __str__ 方法，這是因為 __str__ 方法會優先於 __repr__ 方法
print(s0)
