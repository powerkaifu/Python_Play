'''
錯誤分為語法錯誤(Synatax error) 與 語意錯誤(Semantic error)
語法錯誤是不符合語法規則，無法執行
語意錯誤是符合語法規則，但是執行時期會出錯，可以用 try except 來捕捉處理
'''

# 語法錯誤(Synatax error)
## 少了冒號
'''
if 5>3
  print("5>3")
'''

# 語意錯誤(Semantic error)
## ZeroDivisionError
'''
result = 5 / 0 # ZeroDivisionError: division by zero
'''

## TypeError
'''
5 > 'a' # TypeError: '>' not supported between instances of 'int' and 'str'
result = 5 + "abc" # TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

## IndexError
'''
'Python'[9] # IndexError: string index out of range
'''

## NameError
'''
i+6 # NameError: name 'i' is not defined
'''
