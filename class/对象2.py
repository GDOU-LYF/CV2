class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1
a=[]
for i in range(1,20):
    a.append(Student(str(i)))

print(Student.count)
