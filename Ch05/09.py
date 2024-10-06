h = int(input('請輸入一個時數：'))
money = 0
if h > 12:
  remain_h = h - 12
  money = 12 * 40 + remain_h * 30
else:
  money = h * 40

print(f'停車 {h} 小時，應繳 {money} 元')
