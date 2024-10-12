from datetime import datetime

now = datetime.now()
year = now.year

count = 0
for i in range(1, year + 1):
  if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
    count = count + 1

print(f'一共經歷了{count} 個閏年')
