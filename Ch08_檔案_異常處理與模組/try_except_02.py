# 捕捉 ZeroDivisionError 異常

try:
  6 / 0
except ZeroDivisionError:
  print("不能除以零")

print('-' * 30)

# 捕捉 TypeError 異常
try:
  5 > 'a'
except TypeError:
  print("型別不符合")

print('-' * 30)

# 捕捉 IndexError 異常
try:
  'python'[9]
except IndexError:
  print("索引超出範圍")

print('-' * 30)

# e
try:
  'python'[9]
except Exception as e:
  print(e)

print('-' * 30)

# 捕捉 NameError 異常
try:
  i + 6
except Exception as e:
  print(e)

print('-' * 30)

# try-except-else-finally
try:
  a = 12 + 6
except Exception as e:
  print(e)
else:
  print("沒有發生異常")
finally:
  print("這段一定會執行")

print('-' * 30)
