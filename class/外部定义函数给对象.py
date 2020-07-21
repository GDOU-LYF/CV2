class Student(object):
    __slots__ = ('name', 'age') 
    # 用tuple定义允许绑定的属性名称

def set_age(self,age):
    self.age=age

from types import MethodType
s=Student()
s.name='MS'
s.set_age=MethodType(set_age,s) #仅仅对s有效
s.set_age(25)
print(s.name,s.age)

def set_Score(self,score):
    self.score=score
Student.set_Score=set_Score
s.set_Score(20)
print(s.score)