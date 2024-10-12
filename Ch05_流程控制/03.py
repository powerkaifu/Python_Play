# 閏年
year = int(input("請輸入一個年份:"))

## 可以被 400 整除，或者 被 4 整除，但不能被 100 整除
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
  print(f"{year} 是閏年")
else:
  print(f"{year} 不是閏年")
