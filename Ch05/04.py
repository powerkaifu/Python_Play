a = int(input('讀入數字1：'))
b = int(input('讀入數字2：'))
c = int(input('讀入數字3：'))

lst = sorted([ a, b, c ])
d, e, f = lst

if d**2 + e**2 >= f**2:
  print(f'({a},{b},{c}) 可以構成一個三角形')
else:
  print(f'({a},{b},{c}) 無法構成一個三角形')
