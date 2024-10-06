# lst = [ 1, 3, 2, 4 ]
# print(sum(lst))

# total = 0
# for item in lst:
#   total += item

# print(total)

# lst = [ 1, 9, 0, 3, 6, 2 ]
# total = 1

# for item in lst:
#   if item % 2 == 0 and item != 0:
#     total *= item

# print(total)

# lst = []

# for item in range(0, 10):
#   lst.append(item**2)

# print(lst)

# lst = [ 45, 87, 56, 12, 96, 54 ]
# print(max(lst))

# max = 0

# for item in lst:
#   if item > max:
#     max = item

# print(max)

# keys = [ 'pie', 'candy', 'tea']
# values = [ 30, 60, 45 ]
# d1 = {}

# for i in range(len(keys)):
#   d1.update({keys[i]: values[i]})

# d1 = dict(zip(keys, values))

# 生成式
# d1 = { key: value for key, value in zip(keys, values) }

# print(d1)

# s1 = "01234"
# s2 = "Hello"

# a = zip(s1, s2)

# for k, v in a:
#   print(k, v)

lst = [( 2, 3 ), ( 2, 4 ), ( 3, 2 ), ( 2, 5 )]
for item in lst:
  base, p = item
  print(f'{base}**{p} = {base**p:3d}')
