
class Student:

    # 定义类变量，在方法体外，不属于具体实例方法
    number = 0

    # 定义学生属性，初始化方法
    # name和score属于实例变量，其中__score属于私有变量
    def __init__(self, name, score):
        self.name = name
        # self.score = score
        self.__score = score


        Student.number = Student.number + 1


    # 定义打印学生信息的方法
    def show(self):
        print("name:{}, Score:{}".format(self.name, self.__score))

    @property #把函数伪装成属性
    def score(self):
        print("name:{}, Score:{}".format(self.name, self.__score))



    # 定义类方法
    @classmethod
    def total(cls):
        print("Total:{0}".format(cls.number))
        


student1 = Student("su", 100)
student1.show()
student1.score
# print(Student.number)

# student2 = Student("susen", 90)
# print(student1.__class__.number)
# Student.total()



        