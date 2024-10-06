x = int(input("輸入一個 x 值: "))
if x % 2 == 1:
  print(f"{x} 是奇數")
else:
  print(f"{x} 是偶數")

# 條件運算子(類似三元運算子)
print(f"{x} 是奇數") if x % 2 == 1 else print(f"{x} 是偶數")
