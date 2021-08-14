#25.自定义模块（模块中含有变量、函数、类），然后使用该模块（两种方法），并使用模块中的内容
a = 100

def add(x,y):
    return x+y

class Car:
    def __init__(self,skill,color):
        self.skill = skill
        self.color = color
        print(self.skill,self.color)



