'''
學號：511171017
姓名：張凱富
'''

# 定義一個生成器


def gen(n):
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 != 0:
      yield i


# 產生一個生成器對象
gi = gen(10)

# 使用 next() 函數獲取下一個值
while True:
  try:
    print(next(gi))
  except StopIteration:
    break

print('-' * 30)

# 使用產生器生成式
gi = ( x for x in range(1, 11) if x % 3 == 0 and x % 5 != 0 )

# 使用 next() 函數獲取下一個值
while True:
  try:
    print(next(gi))
  except StopIteration:
    break
