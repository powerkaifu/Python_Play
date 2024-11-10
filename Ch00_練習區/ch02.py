# ord 顯示 ASCII 碼
ord('a')  # 97

# is not 是檢查是否引用相同一個記憶體位置
a = 10
b = 5
print(a is not b)

# != 是檢查兩個變數的值是否相等
a = [ 1, 2, 3 ]
b = [ 1, 2, 3 ]

print(a == b)

print('-' * 30)

print(not 2**3 < 10)  # False

# 0、''、None、[] 都是 False
bool(0)  # False
bool('')  # False
bool(None)  # False
bool([])  # False

bool(-1)  # True
bool('a')  # True
bool([1])  # True

# 進位轉換
bin(10)  # '0b1010'
oct(10)  # '0o12'
hex(10)  # '0xa'

int('1010', 2)  # 10
int('12', 8)  # 10
int('a', 16)  # 10
