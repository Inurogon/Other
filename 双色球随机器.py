#双色球随机器
import random
a={}
b={}
c=int(input('请问你要买几组:'))
for i in range(c):
    list_red={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33}
    a=random.sample(list_red,6)
    print('红色：',end='')
    print(a)
    list_blue={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
    b=random.sample(list_blue,1)
    print('蓝色：',end='')
    print(b)
d=str(c*2)
print('一共是'+d+'元,谢谢您的光临')


