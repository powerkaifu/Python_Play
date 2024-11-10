while True:
  n = input('輸入一個數字:')
  if n in 'qQ':
    print('結束程式')
    break
  else:
    try:
      print(int(n)**2)
    except Exception as e:
      print(e, '請輸入數字!!!!!')
