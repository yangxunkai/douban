class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        #这是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法

    def displayCount(self):
        print
        ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
emp1 = Employee("adxasd",2000)

emp2=Employee("aer",5000)

emp1.age=7

#del emp1.age

setattr(emp1,'age1',8)
print(delattr(emp1,'age1'))
emp1.displayEmployee()
emp2.displayEmployee()

print("职员的人数为：%d" % Employee.empCount)