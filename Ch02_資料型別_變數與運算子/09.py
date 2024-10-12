# (a) 2+True
print(2 + True)  # 3

# (b) 6+int(17.4)
print(6 + int(17.4))  # 23

# (c) 21+6.5
print(21 + 6.5)  # 27.5

# (d) str(2) + 'piggy'
print(str(2) + 'piggy')  # 2piggy

# (e) 2 + 'piggy'
## 數字與字串無法相加
print(2 + 'piggy')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
