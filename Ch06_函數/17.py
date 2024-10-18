'''
學號：511171017
姓名：張凱富
'''


# 定義函式
def make_dict(key, values = None):
  # 如果 values 為 None(未指定)，則建立一個元素值為 0 的列表
  if values is None:
    values = [0] * len(key)

  if len(key) == len(values):
    # zip() 函式將兩個序列合併成一個元組的列表
    return dict(zip(key, values))


key = [ 0, 1, 2 ]
values = [ 32, 43, 55 ]

# 呼叫函式與打印結果
result1 = make_dict(key, values)
print(result1)

# 呼叫函式與打印結果
result2 = make_dict(key)
print(result2)
