#22.新建一个文件并且向文件中追加写入“我是XXX”，然后关闭文件
'''
file = open("a.txt","a")
file.write("我是XXX")
file.close()

'''


#23.获取当前工作目录，并且在当前工作目录新建一个"aaa"目录，并且将其重命名为"bbb"
'''
import os
print(os.getcwd())
#os.mkdir("aaa")
os.rename("aaa","bbb")

'''

#24.定义一个学生类，公有属性name、age，私有属性ID，第一个公有方法用来设置私有属性ID，第二个方法用来获取私有属性ID(name和age的值由实例化对象时传入)，然后实例化一个对象，并且修改和获取ID

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__id = 123

    def set(self,id):
        self.__id = id

    def get(self):
        a = self.__id
        return a

s1 = Student("roy",20)

print(s1.get())
s1.set(123456)
print(s1.get())
