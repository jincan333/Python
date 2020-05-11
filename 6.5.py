#利用turtle模块画一棵树，包括枝干和树叶，并涂上颜色
import turtle
import random
turtle.screensize(10000,10000)
turtle.Turtle().screen.delay(0)               #取消延迟，有奇效
p=turtle.Pen()
p.speed(0)                                    #笔尖速度调至最大
p.color('Goldenrod4')                         #树干颜色
p.seth(90)                                    #调整初始角度
pos=[[],[],[],[],[],[],[],[],[],[]]           #记录枝干节点位置
pos[0].append(p.pos())                        #将枝干节点位置存储到列表中
for i in range(6):                            #枝干层数
    for pos_ in  pos[i]:
        for j in range(round((3/2)**i)):      #每个枝干节点的分叉数
            p.penup()                         #提笔并在枝干节点之间移动
            p.goto(pos_)
            p.pendown()
            p.width(60*(4/7)**i)              #枝干宽度
            p.forward(200*(11/12)**i)          #枝干长度
            pos[i+1].append(p.pos())          #在列表中添加枝干接点
            a=random.randint(-75,75)          #设置枝干方向
            p.seth(a+90)
p.color('green')                              #叶子颜色
p.seth(90)
for i in range(4,7):
    for pos_ in  pos[i]:
        for j in range(12):                   #每个枝干节点处的叶子数
            p.penup()
            p.goto(pos_)
            p.pendown()
            p.width(20*(4/5)**i)              #叶片宽度
            p.forward(40)                     #叶片长度
            a=random.randint(-90,90)          #叶片方向
            p.seth(a+90)
turtle.mainloop()                             #显示绘图窗口
