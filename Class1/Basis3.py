# 函数
a, b, c = 3, 4, 5

# def=define 定义
def fun(x, y, z):
    return x + y > z and x * x + y * y == z * z

if fun(a, b, c) or fun(b, c, a) or fun(c, a, b):
    print("可以构成三角形")

# 面向对象

s = "ABC"

# 点号：成员访问符，可以理解为“的”
print(s.lower())

# 定义一个类
class Person:
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法(实例函数)
    def introduce(self):
        print("My name is " + self.name + ", I am " + str(self.age) + " years old.")

# 创建一个对象(类的实例)
p = Person("Alice", 20)

# 调用对象的方法
p.introduce()
