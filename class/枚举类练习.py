from enum import Enum, unique
@unique
class Gender(Enum):
    Male = 1
    Female = 2

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        # Gender=Enum(self.name,self.gender)

bart = Student('Bart', Gender.Female)
if bart.gender == Gender.Female:
    print('测试通过!')
else:
    print('测试失败!')