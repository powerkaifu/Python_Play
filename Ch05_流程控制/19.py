import math

a = int(input('請輸入 a：'))
b = int(input('請輸入 b：'))

if a > b:
  a, b = b, a

# 最大公因數，兩個數字中能夠整除的最大數字，1 是最小的最大公因數
gcd = 1
for i in range(1, b + 1):
  if a % i == 0 and b % i == 0:
    gcd = i

print(gcd)

# 可以用 math.gcd() 解最大公因數
gcd2 = math.gcd(a, b)

print(gcd)
