d1 = {
    0: 'red',
    1: 'green',
    2: 'blue',
}

# (a) 查詢 d1 的鍵 1 值
print(d1[1])

# (b) 鍵 2 設定為 'yellow'
d1[2] = 'yellow'
print(d1)

# (c) 刪除 d1 的鍵 0 值對
del d1[0]
print(d1)

# (d) 查詢鍵 4 是否存在
print(4 in d1)
