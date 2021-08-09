
# 创建父类学校成员SchoolMember
class SchoolMember: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def tell(self):
        # 打印个人信息
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


#创建子类老师 Teacher
class Teacher(SchoolMember): 
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self, name, age) #利用父类进行初始化
        self.salary = salary
    #方法重写
    def tell(self):
        # SchoolMember.tell(self)
        super().tell()
        print("Salary:{}".format(self.salary))


# 创建子类学生Student
class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score
    def tell(self):
        # SchoolMember.tell(self)
        super().tell() #调用父类的方法
        print("score:{}".format(self.score))


teacher1 = Teacher("su", 21, "$6666")
student1 = Student("susen", 12, 99)
teacher1.tell()
student1.tell()
        
        
