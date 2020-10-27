class Parent:
    def myMethod(selfself):
        print("调用父类方法")
#子类重载父类方法
class Child(Parent):
    def myMethod(selfself):
        print("调用子类方法")

c=Child()
c.myMethod()