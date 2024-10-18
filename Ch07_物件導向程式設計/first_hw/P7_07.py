'''
學號：511171017
姓名：張凱富
'''


# 定義類別
class Employee:
  payRate = [ 1, 1.2, 1.5 ]  # 給付比率

  def __init__(self, base):
    self.baseSalary = base  # 基本薪資

  # (a) 計算薪資
  def salary(self, hr, bonus):
    if bonus < 0 or bonus >= len(self.payRate):
      return 'bonus 不在範圍內'
    return int(self.baseSalary * hr * self.payRate[bonus])  # 基本薪資 * 小時數 * 給付比率

  # (b) 設定給付比率，它是類別方法
  @classmethod
  def set_payRate(cls, new_payRate):

    try:
      if not isinstance(new_payRate, list):
        print('必須是 list')
        return
      cls.payRate = [float(rate) for rate in new_payRate]  # 轉換成浮點數，如果無法轉換會發生 ValueError
    except ValueError:  # 檢查是否為數字
      print('有非數字的元素')
    except Exception as e:
      print(f'發生其他錯誤: {e}')

  # (c) 估算薪資，它是靜態方法，不需要 cls，因為沒有修改類別屬性
  @staticmethod
  def estimate(bs, hr, rate):
    return int(bs * hr * rate)


# 進行測試
tom = Employee(160)
# (a) 的測試
print('-' * 10, '(a) 測試', '-' * 10)
print(tom.salary(10, 1))  # 1920

# (b) 的測試
print('-' * 10, '(b) 測試', '-' * 10)
Employee.set_payRate([ 1, 1.3, 1.5 ])
print(tom.salary(10, 1))  # 2080

# (c) 的測試
print('-' * 10, '(c) 測試', '-' * 10)
print(Employee.estimate(160, 10, 1.25))  # 2000

# 例外處理
print('-' * 10, '例外處理', '-' * 10)
print(tom.salary(10, -1))  # bonus 不能是負數
print(tom.salary(10, 10))  # 超過給付比率的長度
Employee.set_payRate("我是字串")  # 必須是一個 list
Employee.set_payRate([ 1, "我是字串", 1.6 ])  # list 必須是數字
