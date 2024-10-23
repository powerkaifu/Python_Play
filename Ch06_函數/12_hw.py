'''
學號：511171017
姓名：張凱富
'''


# 定義函式
def combine(t1, t2):
  # 檢查是否為 tuple
  if not isinstance(t1, tuple) or not isinstance(t2, tuple):
    raise TypeError("兩個都必須是 tuple！")
  else:
    return t1 + t2


# 呼叫函式
result = combine([ 1, 2 ], ( 2, 5, 6 ))

# 打印結果
print(result)
