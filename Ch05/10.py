s = int(input('請輸入一個整數，s < 86400：'))
remain_time = s

if remain_time < 86400:
  hour = remain_time // (60 * 60)  # // 取整數
  remain_time = remain_time % (60 * 60)
  minute = remain_time // 60
  remain_time = remain_time % 60
  sec = remain_time
  print(f'{s}秒等於{hour}小時{minute}分{sec}秒')
else:
  print('請輸入小於 86400')
