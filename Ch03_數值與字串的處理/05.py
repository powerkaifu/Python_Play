# 字串 *^_^* 打印 10 次
print('*^_^*' * 10)

# 設 s1 = 'Have a nice day'
s1 = 'Have a nice day'

## (a) 提取 nice 子字串
print(s1[7 : 11])

## (b) 判斷 day 是否在 s1 中
print('day' in s1)

## (c) 提取 s1 的最後一個字元
print(s1[-1])

## (d) 找出 s1 內，字元編碼最大的字元
print(max(s1))

# 設 s2 = 'it is never too late to learn'
s2 = 'it is never too late to learn'

## (a) 將 s2 的每一個單字的第一個字母轉換為大寫
print(s2.title())

## (b) 將 s2 的第一個字母轉換為大寫
print(s2.capitalize())

## (c) 測試 s1 是否全為英文字母
print(s2.isalpha())

## (d) 計算字元 'e' 在 s2 中出現的次數
print(s2.count('e'))

## (e) 刪除掉 never 這個單字
s2_new = s2.replace('never ', '')
print(s2_new)

## (f) 把 late 換成 LATE
s2_new = s2.replace('late', 'LATE')
print(s2_new)
