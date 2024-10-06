while True:
  x = int(input("請輸入一個 x："))

  if x <= 0:
    break

  if x >= 90:
    print("A")
  elif x >= 80:
    print("B")
  elif x >= 70:
    print("C")
  elif x >= 60:
    print("D")
  else:
    print("E")
