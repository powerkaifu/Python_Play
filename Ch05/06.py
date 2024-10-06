a = int(input('讀入數字1：'))
b = int(input('讀入數字2：'))
c = int(input('讀入數字3：'))

if a > b:
  tmp = a
  a = b
  b = tmp

if b > c:
  tmp = b
  b = c
  c = tmp

if a > b:
  tmp = a
  a = b
  b = tmp

print(a, b, c)
