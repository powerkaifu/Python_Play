lst = [
    [ 2, 4, 5 ],
    [ 5, 8, None ],
    [ 10, 3, 4 ],
]

for index, datas in enumerate(lst):
  isNone = False
  for data in datas:
    if data is None:
      isNone = True
      break
  if not isNone:
    print(f'第 {index} 組：{sum(datas)}')
  else:
    print(f'第 {index + 1} 組：Incomplete data')

print('-' * 30)

# any() 是 Python 內建函數，用來判斷可迭代物件中是否有任一元素為 True

for index, datas in enumerate(lst):
  if any(data is None for data in datas):
    print(f'第 {index + 1} 組：Incomplete data')
  else:
    print(f'第 {index} 組：{sum(datas)}')
