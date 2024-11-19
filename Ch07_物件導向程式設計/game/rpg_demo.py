from rpg import SwordsMan, Magician, Duck

swordsman = SwordsMan('Justin', 1, 200)
print(swordsman)  # 劍士 (Justin, 1, 200)

magician = Magician('Monica', 1, 100)
print(magician)  # 魔法師 (Monica, 1, 100)

# 鴨子型別
## 動態語言界流行的概念:如果它走路像個鴨子，叫聲像個鴨子，那麼它就是個鴨子
## 動態語言應該思考物件的行為，而不是物件的類別
## 因為不會檢查型別，每個物件都可以當作參數傳入函數，所以可以做同樣的事情

# def draw_fight(role):
#   print(role, end = ' ')
#   role.fight()

print('-' * 30)


# 防止鴨子型別
def draw_fight(role):
  if isinstance(role, SwordsMan):
    print('一位劍士', end = ' ')
  elif isinstance(role, Magician):
    print('一位魔法師', end = ' ')
  else:
    print('不符合的角色', end = ' ')
    return
  print(role, end = ' ')
  role.fight()


draw_fight(swordsman)  # 劍士 (Justin, 1, 200) 揮劍攻擊
draw_fight(magician)  # 魔法師 (Monica, 1, 100) 魔法攻擊

duck = Duck()
duck.fight = lambda: print('呱呱呱')
draw_fight(duck)  # <__main__.Duck object at 0x000001E1D3D3A4C0> 呱呱呱
