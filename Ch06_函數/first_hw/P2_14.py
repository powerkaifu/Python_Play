'''
學號：511171017
姓名：張凱富
'''


# 定義函式
def add_n(lst, n):
  # 檢查是否為串列
  if not isinstance(lst, list):
    raise TypeError('lst 必須為串列！')
  return [x + n for x in lst]


# 呼叫函式
lst = [ 10, 20, 30, 40, 50 ]
result = add_n(lst, 1)

# 打印結果
print(result)
