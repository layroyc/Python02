#16-21

#16.定义一个空列表list1，然后向列表中添加你的名字、年龄、身高、体重四项数据

list1 = list()
a = input("请输入你的姓名")
list1.append(a)
b = input("请输入你的年龄")
list1.append(b)
c = input("请输入你的身高")
list1.append(c)
d = input("请输入你的体重")
list1.append(d)
print(list1)


#17.定义两个列表，分别进行+操作和*操作
a = [12,15]
b = [1,2,6]

print(a+b)
print(a*2)


#18.定义一个元组，输出元素长度，并且对元组进行解包
w = (2,3,5)
#print("元组的长度为：",len(w))
x,y,z=w
print(x)
print(y)
print(z)


#19.定义一个字典，字典内容写入你的信息，并且遍历出键和键对应的值
roy = {
    "name":"wy",
    "age":"20",
    "sex":"男",
    "hobby":["singsong","write","tan"]
    }

for i in roy:
    print("%s : %s" % (i,roy[i]))



#20.定义一个集合
#   可变集合
w = {1,2,3,4,5}
y = set([2,5,7,9])
print(w)
print(y)

#   不可变集合
r = frozenset([7,8,9,10])
print(r)
print(type(r))


#21.定义一个函数，一个全局变量和局部变量，并且在函数内部修改全局变量的值，并且在函数内部返回这两个变量
w = 16
def func():
    y = 21
    #在函数内部有效修改全局变量
    global w
    #函数内部访问全局变量
    print(w)
    w = 24
    return w,y
print(func())
print(w)



