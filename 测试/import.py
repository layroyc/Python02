'''
# 导入模块 import
import test
print(test.a)
print(test.add(5,9))
s1 = test.Car("能跑","block")

# 导入模块 from
from test import *
print(a)
print(add(2,7))

s2 = test.Car("能住","yellow")
'''

'''
w = 1
while w<10:
    y = 1
    while y<=w:
        print('%d*%d=%2d' % (w,y,w*y),end=' ')
        y+=1
    print()
    w+=1
'''


list1 = [3, 6, 9, 11, 8, 56, 4]

def sort_list(list):
    n = len(list)
    i = 0
    j = i
    for i in range(n-1):
        for j in range(n-1-i):
            if list[j] < list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]

sort_list(list1)
print(list1)



