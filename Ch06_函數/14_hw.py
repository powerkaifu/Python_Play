'''
學號：511171017
姓名：張凱富
'''


# 定義函式
def add_n(lst, n = 0):
  # 檢查是否為串列
  if not isinstance(lst, list):
    raise TypeError('lst 必須為串列！')
  return [x + n for x in lst]


# 呼叫函式，並傳入參數
lst = [ 10, 20, 30, 40, 50 ]
result = add_n(lst, 1)

# 呼叫函式，沒有傳入參數，預設 n = 0
lst2 = [ 1, 2, 3, 4, 5 ]
result2 = add_n(lst2)

# 打印結果
print(result)
print(result2)
