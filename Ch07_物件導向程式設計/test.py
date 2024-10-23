class Student:
  grade = 70  # 類別屬性

  def show(self):
    print('grade=', self.grade)


tom = Student()
print('tom.grade=', tom.grade)  # 70，使用類別屬性
tom.show()  # grade= 70
tom.grade = 80
print('tom.grade=', tom.grade)  # 90，使用實例屬性

# print(isinstance(tom, Student))

print(hasattr(tom, 'grade'))
setattr(tom, 'grade', 100)
print(tom.grade)
print(getattr(tom, 'grade'))
