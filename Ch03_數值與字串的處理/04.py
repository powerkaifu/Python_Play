import random

# (a) 隨機取出 1 ~ 100 之間的亂數
print(random.randrange(1, 100))

# (b) 隨機取出 s1 中的 3 個字元
s1 = 'Halloween'
s1_list = random.sample(s1, 3)
print(''.join(s1_list))

# (c) 隨機取出 lst 中的 3 個元素
lst = [ 12, 38, 54, 64, 77, 29 ]
lst_random = random.sample(lst, 3)
print(lst_random)

# (d) 將 lst 中的元素隨機排序
my_lst = [ 2, 3, 5, 8, 9 ]
random.shuffle(my_lst)
print(my_lst)
