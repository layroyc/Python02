#12.判断分数区间，分数等于100奖励大餐一顿，90分以上奖励玩游戏两个小时，60-90分鼓励继续加油，60分一下奖励试卷十套
'''
sum = int(input("请输入成绩:"))

if sum ==100:
    print("奖励大餐一顿")
elif 90 < sum < 100:
    print("奖励玩游戏两个小时")
elif 60 < sum < 90:
    print("继续加油")
elif 0 < sum < 60:
    print("奖励试卷十套")
else:
    print("输入错误，请重新输入")

'''

#13.使用三元运算符输出两数中的较大值

w = 20
y = 8
max = 'w' if w>y else 'b'
print(max)


# 14.分别使用while循环和for循环输出1-100之间的偶数
i=1
while i<=100:
    if i%2==0:
        print("%d是偶数" %i)
    i+=1
print('===========')
for s in range(2,101,2):
    print("%d是偶数" % s)


#15.定义账号变量为“smxzy”，密码变量为“123456”，定义一个死循环输入账号和密码，都输入正确提示登陆成功，否则继续循环输入

w ="smxzy"
y = "123456"

a = True

while a:
    x = input("请输入账号:")
    z = input("请输入密码:")
    if x == w and z == y:
        print("登陆成功")
        break
    continue
