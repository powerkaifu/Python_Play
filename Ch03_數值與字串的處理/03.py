import random
# (a)
print(random.random())  # 0 ~ 1 之間的亂數

# (b)
s = 'Significant'
for i in range(1, 4):
  print(random.choice(s), sep = '', end = '')

print("")

s2 = 'Significant'
random_chars = random.sample(s2, 3)  # 返回一個列表，包含 3 個不重複的隨機字符
print(''.join(random_chars))

# (c)
print(random.randint(1, 6))  # 1 ~ 6 之間的亂數

# (d)
print(random.randrange(2, 10, 2))  # 1 ~ 10 之間的偶數亂數

# (e)
print(random.uniform(-1, 1))  # -1 ~ 1 之間的亂數
