class Account:
  __bankname = 'Taipei Bank'  # 雙底線表示私有變數

  # class 的函數第一個參數是 self，代表實例物件本身
  def __init__(self, name, number, balance) -> None:  # 建構子
    self.__name = name  # 雙底線表示私有變數
    self.__number = number
    self.__balance = balance  # 餘額

  @property  # getter 裝飾器，將方法變成屬性，可以直接讀取屬性值，acct.name
  def name(self) -> str:
    return self.__name

  @name.setter  # setter 裝飾器，可以修改屬性值，acct.name = 'Justin'
  def name(self, name):
    self.__name = name

  @property
  def number(self) -> str:
    return self.__number

  @number.setter
  def number(self, number):
    self.__number = number

  @property
  def balance(self) -> float:
    return self.__balance

  @balance.setter
  def balance(self, balance):
    self.__balance = balance

  def deposit(self, amount):  # 存款
    if amount <= 0:
      print('存款金額必須大於 0')
    else:
      self.__balance += amount

  def withdraw(self, amount):  # 提款
    if amount > self.__balance:
      print('餘額不足')
    else:
      self.__balance -= amount

  def check_balance(self):  # 查詢餘額
    print(f'餘額：{self.__balance}')

  @staticmethod  # 靜態方法，不需要任何參數，不能修改類別屬性
  def bankname() -> str:
    return Account.__bankname

  @classmethod  # 類別方法，第一個參數是 cls，代表類別本身
  def get_bankname(cls) -> str:
    cls.__bankname = 'KaiFu Bank'
    return cls.__bankname

  def __str__(self):
    return f'Account({self.__name!r}, {self.__number!r}, {self.__balance})'

  def __repr__(self):
    return f'Account(name={self.__name!r}, number={self.__number!r}, balance={self.__balance!r})'
