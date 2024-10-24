# gererator 使用類似串列生成式的語法，差異在於使用 () 來建立
# 並使用 next() 來取得下一個值

g1 = (i**2 for i in range(3))
print(next(g1))
print(next(g1))
print(next(g1))

print('-' * 30)

g2 = sum((i**2 for i in range(3)))
print(g2)

g3 = sum(i**2 for i in range(3))
print(g3)

lst1 = sum([i**2 for i in range(3)])
print(lst1)

print('-' * 30)


# 生成器函式
def gen_func():
  for i in range(3):
    yield i**2


gen = gen_func()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4


# 模擬 range()
def xrange(n):
  x = 0
  while x != n:
    yield x
    x += 1


for i in xrange(10):
  print(i)
