while True:
  t = int(input('請輸入溫度'))
  if t == 0:
    break
  if t == 20:
    print(f"現在溫度為{t}度，不開冷暖氣")
  elif t < 15:
    print(f"開暖氣")
  elif t > 28:
    print(f"開冷氣")
