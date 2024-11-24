# 單例模式
class Singleton:
  __instance = None

  # __new__ 是在 __init__ 之前被呼叫的特殊方法，可以用來返回一個新的實例
  # 由於是靜態方法，所以第一個參數是 cls，而不是 self
  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)  # super() 指的是父類別，這裡指 object，這邊的 cls 是指 Singleton
    return cls.__instance


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True

print('-' * 30)
