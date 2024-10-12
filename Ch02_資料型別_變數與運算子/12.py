# 試著讀入一個整數，計算平方之後，再將結果印出來。
num1 = int(input('請輸入一個整數：'))
print(num1**2)

# 試著讀入一個整數，把它轉成 2 進位後，再印出來。
num2 = int(input('請輸入一個整數：'))
print(bin(num2))

# 如何擷取省略 0b 的 2 進位字串
num3 = int(input('請輸入一個整數：'))
print(type(bin(num3)))  # <class 'str'>
print(bin(num3)[2 :])
