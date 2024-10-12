# if month >= 3 and month <= 5:
#   print(f'{month} 月為春季')
# elif month >= 6 and month <= 8:
#   print(f'{month} 月為夏季')
# elif month >= 9 and month <= 11:
#   print(f'{month} 月為秋季')
# else:
#   print(f'{month} 月為冬季')

while True:
  month = int(input('請輸入一個月份：'))

  if month < 1 or month > 12:
    print('請輸入有效的月份 1 - 12')
    break

  if month in [ 3, 4, 5 ]:
    print(f'{month} 月為春季')
  elif month in [ 6, 7, 8 ]:
    print(f'{month} 月為夏季')
  elif month in [ 9, 10, 11 ]:
    print(f'{month} 月為秋季')
  else:
    print(f'{month} 月為冬季')
