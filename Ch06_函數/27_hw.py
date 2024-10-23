'''
學號：511171017
姓名：張凱富
'''

# 檢測資料
lst = [-3, 6, 100, 300]

# 第一種方法 lambda + Comprehension(生成式) 進行篩選
numbers_0_to_255 = lambda lst: [ x for x in lst if x >= 0 and x <= 255 ]
# 打印結果
print(numbers_0_to_255(lst))

print('-' * 30)

# 第二種方法，lambda + filter() 函式
numbers_0_to_255_2 = list(filter(lambda x: x >= 0 and x <= 255, lst))
print(list(numbers_0_to_255_2))

print('-' * 30)


# 第三種方法，filter + 一般函式
def check_number(x):
  return 0 <= x <= 255


numbers_0_to_255_3 = list(filter(check_number, lst))
print(numbers_0_to_255_3)
