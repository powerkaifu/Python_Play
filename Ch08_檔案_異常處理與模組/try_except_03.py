try:
  input = int(input("輸入整數:"))
  print(input)
except ValueError as e:
  print("請輸入阿拉伯數字：", e)
else:
  print("沒有例外發生")
finally:
  print("這段一定會執行")

# 補捉不能除以零的例外
try:
  result = 10 / 0
except ZeroDivisionError as e:
  print(type(e))  # <class 'ZeroDivisionError'>
  print('打印出例外名稱：', type(e).__name__)
  print("不能除以零:", e)

# 捕捉多個例外

try:
  result = int("abc")
except ( ValueError, TypeError ) as e:
  print("轉換錯誤:", e)

# 使用 else 語句
# 如果 try 塊中沒有引發例外，則執行 else 塊中的代碼。
try:
  result = 10 / 2
except ZeroDivisionError as e:
  print("不能除以零:", e)
else:
  print("計算成功:", result)
