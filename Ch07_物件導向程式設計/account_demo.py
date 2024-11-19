from account import Account

acct = Account('Justin', '123-4567', 1000)  # 建立實例物件，會呼叫 __init__ 函數，將物件傳入第一個參數 self
acct.deposit(500)  # 存款 500 元
acct.withdraw(200)  # 提款 200 元
acct.check_balance()  # 查詢餘額

print(acct)  # 會呼叫 __str__ 函數，Account(Justin, 123-4567, 1000)
print(str(acct))  # 會呼叫 __str__ 函數，Account(Justin, 123-4567, 1000)
print(repr(acct))  # 會呼叫 __repr__ 函數，Account(name='Justin', number='123-4567', balance=1000)

# 透過 @property 裝飾器可以直接讀取屬性值
print(acct.name)  # Justin
print(acct.number)  # 123-4567
print(acct.balance)  # 1300

# 透過 @setter 裝飾器可以修改屬性值
acct.name = 'KaiFu'
acct.number = '100-2000'
acct.balanc = 30000

print(acct.name)  # KaiFu
print(acct.number)  # 100-2000
print(acct.balance)  # 1300

print('-' * 30)

# 靜態方法
print(Account.bankname())  # Taipei Bank

# 類別方法
print(Account.get_bankname())  # Taipei Bank
