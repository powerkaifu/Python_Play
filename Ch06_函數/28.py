lst = [-3, 6, -4, 6, 8]
new_list = list(map(lambda x: 0 if x < 0 else x, lst))
print(new_list)
