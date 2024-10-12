import math

n = int(input('請輸入一個數：'))

result = 1
for i in range(1, n + 1):
  result = result * i

print(result)

# 使用 math.factorial
result2 = math.factorial(n)
print(result2)
