# _*_ coding:utf-8 _*_
from  math import *
'''
打印100~300间的全部素数
'''
def printSS():
    ssArr=[]
    for i in range(100,301):
        for j in range(2,i):
            if i%j==0:
               break;
            elif j==i-1:
                ssArr.append(i)
        if len(ssArr)%8==0 and len(ssArr)!=0 :
            print(ssArr)
            print(r'[----1----]')
            ssArr=[]
#printSS()
'''
打印如下图案
    1
   1 2
  1 2 4
 1 2 4 8
1 2 4 8 16
 1 2 4 8
  1 2 4
   1 2
    1
'''
def printDevice():
     for i in range(1,10):
         s=''
         if i <=5:
            for j in  range(0,i):
                s+=str(2**j)+' '
         else:
             for j in range(0,10-i):
                 s+=str(2**j)+' '
         print(s.center(10))
#printDevice()
'''
编写函数，检测给定的两个列表是否有重复数据（假设都是整数），
如果没有重复，返回为真，如果重复返回具有重复值的列表
'''
def judgeRepetition(a,b):
    repetitions=[]
    if isinstance(a,list) and isinstance(b,list):
        for item_a in a:
            for item1_b in b:
                if item_a==item1_b:
                    repetitions.append(item_a)
        if len(repetitions)==0:
            return True
        else:
            return repetitions
    else:
        return '请输入两个数组'
#print(judgeRepetition([1,2,3,4,5],[2,3,4,5,6,7]))
#print(judgeRepetition([1,2,3,4,5],[7,8,9,13,21,71]))
'''
编写一个函数，输入一元二次方程系数a,b,c,若有实数根，求根并输出，否则输出‘不是二次方程或没有实数根’的信息
当a=0时 不是一元二次方程
当b^2-4ac<0  没有实数根
当b^2-4ac>0 有实数根 -b+√(b^2-4ac)/2a -b-√(b^2-4ac)/2a 
'''
def solveEquation(a,b,c):
    if isinstance(a,int) or isinstance(a,int) or isinstance(a,int):
        if a ==0:
            return '不是二次方程'
        elif (b**2-4*a*c)<0:
            return  '没有实数根'
        elif (b**2-4*a*c)==0:
            return  -b+sqrt(b**2-4*a*c)
        else:
            return [-b+sqrt(b**2-4*a*c),-b-sqrt(b**2-4*a*c)]
    else:
        return '请传入数字'
#print(solveEquation(1,4,4))
'''
编写一个python函数，求两个正整数的最大公约数如果这两个正整数不在1到1000范围内，就抛出一个自定义异常，
'''
#定义一个异常类
class myError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo
def MAXCommonDivisor(a,b):
    if isinstance(a,int) and isinstance(b,int):
        if 1<=a<=1000 and 1<=b<=1000:
            divisorA=[]
            divisorB = []
            maxDivisor=0
            for a1 in range(1,a+1):
                    if a%a1==0:
                        divisorA.append(a1)
            for b1 in range(1,b+1):
                    if a%a1==0:
                        divisorB.append(b1)
            for maxDivisorA in divisorA:
                for maxDivisorB in divisorB:
                    if maxDivisorA==maxDivisorB:
                        maxDivisor=maxDivisorA
            if maxDivisor!=0:
                return maxDivisor
            else:
                raise myError('没有最大公约数')

        else:
            raise myError('请输入1到1000范围内的整数')
    else:
        raise myError('请输入两个整数')
#print(MAXCommonDivisor(100,10))
'''
在屏幕上输出1！+2！+3！...+n!=的和
'''
def printFactorial(n):
    exp = ''
    result=0
    for i in range(1,n+1):
        factorial = 0
        if i!=n:
            exp+=str(i)+'!+'
        else:
            exp += str(i) + '!='
        for num in range(1,i+1):
            factorial+=num
        result+=factorial
    return exp+str(result)
#print(printFactorial(12))
'''
编写一个python函数,某个公司传递数据,数据是四位的整数,
再传递过程中是加密的,加密规则如下: 每位数字都加上5,然后用除以10的余数代替该数字,
再将第一位和第四位交换,第二位和第三位交换,函数返回加密后的数字.
'''
def encryptData(data):
    if len(str(data))==4 and isinstance(data,int):
        result=''
        strData=list(str(data))
        strData[0],strData[1],strData[2],strData[3]=\
            strData[3],strData[2],strData[1],strData[0]
        for data in strData:
            result+=str((int(data)+5)%10)
        return int(result)
    else:
        raise Exception('请输入四位整数')
#print(encryptData(1234))
'''
按要求编写一个python程序:
(1)定义一个矩形类,描述一个矩形,包含长,宽两种属性,和计算面积的方法.
(2)编写一个长方体类,继承矩形类,同时该类描述长方体,具有长,宽,高属性,和计算体积的方法.
实例化长方体类,验证方法对的正确性,并打印出'长方体的底面积和体积分别是'.
'''
class matrix:
    def __init__(self,length,width):
        self.length=length
        self.width = width
    def getArea(self):
        return self.width*self.length
class cuboid(matrix):
    def __init__(self,length,width,higth):
        super(cuboid, self).__init__(length,width)
        self.higth=higth
    def getVolume(self):
        return self.width*self.length*self.higth
myCuboid=cuboid(1,2,3)
#print('长方体的底面积和体积分别是%i和%i'%(myCuboid.getArea(),myCuboid.getVolume()))
'''
定义一个人类，包括属性：姓名、性别、年龄、国籍；包括方法：吃饭、睡觉，工作。
（1）定义一个学生类继承人类，增加属性：学校、学号；重写工作方法（学生的工作是学习）。
（2）根据学生类，派生一个学生干部类，增加属性：职务；增加方法：开会。
（3）编写主函数分别对上述3类具体人物进行测试。
'''
class person():
    def __init__(self,xm,xb,nl,gj):
        self.xm=xm
        self.xb=xb
        self.nl=nl
        self.gj=gj
    def eat(self):
        print(self.xm+'在吃饭')
    def sleep(self):
        print('睡觉')
    def work(self):
        print('工作')

class student(person):
    def __init__(self,xm,xb,nl,gj,xx,xh):
        super(student,self).__init__(xm,xb,nl,gj)
        self.xx=xx
        self.xh=xh
    def work(self):
        print(self.xm+'说学生的工作是学习')
class studentGB(student):
    def __init__(self,xm,xb,nl,gj,xx,xh,zw):
        super(studentGB, self).__init__(xm,xb,nl,gj,xx,xh)
        self.zw=zw
    def meeting(self):
        print(self.xm+'在开会')
# person1=person('王大江','man','11','SH')
# person1.eat()
# student1=student('王胖1','man','16','nj','nanjUS','100')
# student1.work()
# studentGB1=studentGB('朱胖1','woman','20','nj','nanjUS','90','会长')
# #数组
# a=[1]
# a.append(1) #列表增
# a[0]=2 #列表改
# a.remove(2) #列表删
# print(a)
# a.append(2)
# #字典
# b={}
# b['a']='b' #字典增
# b['a']='c' #字典改
# b.pop('a')#字典删
# #元祖
# c=(1,2,3) #初始化
# print(b)
# c=a #这是浅拷贝，c还是引用的a对象，c的变化还是会影响a的值
# c.append(3)
# print(a)
# print(c)
# d=a.copy() #这是深拷贝，d的变化不会影响a的值
# d.append(4)
# print(a)
# print(d)
#
# f = lambda x: x * x
# print(f(4))
# #此为一个匿名函数
# f = lambda x: x * x
# print(f(4))
# #此为一个普通函数
# def a(x):
#     return x*x
# print(a(4))

#列表
# a=[1] #这是正常赋值
# c=a #这是浅拷贝，c还是引用的a对象，c的变化还是会影响a的值
# c.append(3)
# print(a)
# print(c)
# d=a.copy() #这是深拷贝，d的变化不会影响a的值
# d.append(4)
# print(a)
# print(d)
# a1=10
# a2=a1+2
# a3=a2+2
# a4=a3+2
# a5=a4+2
# print('第五个人%s岁'%a5)
# s='9,5,2,3,4,10,8,6,7'
# list1=s.split(',')
# for i in range(0,len(list1)):
#     for t in range(i+1,len(list1)):
#         if int(list1[t]) <=int(list1[i]):
#             list1[i],list1[t]= list1[t],list1[i]
# print(list1)
def sortList(inputS):
    list1 = inputS.split(',')
    if len(list1)<5:
        print('请输入以英文逗号分割的数字，至少5个')
    else:
        for i in range(0, len(list1)):
            for t in range(i + 1, len(list1)):
                try:
                    if int(list1[t]) <= int(list1[i]):
                        list1[i], list1[t] = list1[t], list1[i]
                except Exception:
                    return '请输入数字'
        return list1
#inputStr = input('请输入至少5个数字用逗号隔开')
#print(sortList(inputStr))


# for x in range(0,len(a)) :
    # temp = []
    # for  y in range(x+1,len(a)):
    #     if a[x]==a[y]:
    #         temp.append(a[y])
    #     else:
    #         temp.append(a[x])
    #         break
    # result.append(temp)

def fgArr(arr):
    result = []
    x = 0
    while (x < len(a)):
        temp = []
        y = x + 1
        temp.append(a[x])
        while (y < len(a)):
            if (a[x] == a[y]):
                temp.append(a[x])
                y = y + 1
            else:
                break
        x = y
        result.append(temp)
    return result
def fgArr2(arr):
    result = []
    start_num = 0
    for x in range(0,len(arr)):
        if x==start_num:
            temp=[]
            temp.append(arr[x])
            for y in range(x+1,len(arr)):
                if arr[x]==arr[y]:
                    temp.append(arr[y])
                else:
                    start_num=y
                    break
        else:
            continue
        result.append(temp)
    return result
a = [1, 1, 0, 2, 2, 2, 4, 3, 3, 4, 2, 0, 0]
#print(fgArr2(a))
def writeFile(filename):
    with open(filename, 'w+', encoding='utf-8') as files:
        while True:
            a=input('请输入文字，输入#停止输入')
            if len(a.split(r'#'))>=2:
                files.write(a.split(r'#')[0]+'\n')
                print('退出文本')
                break
            else:
                files.write(a+'\n')
    files.close()
#writeSomeThing('bbb.txt')
class classes:
    __num__=0
    xs=[]
    def addPerson(self,person):
        self.xs.append(person)
        self.__num__+=1
    def getRS(self):
        print('班级总人数%d'%self.__num__)
class xs(classes):
    def __init__(self,xm,nl,cj):
        self.xm=xm
        self.nl = nl
        self.cj = cj
    def getXM(self):
        print('大家好我叫%s'%self.xm)
    def getnl(self):
        print('姓名%s年龄%s'%(self.xm,self.nl))
    def getcj(self,xk):
        print('这是我的%s:%d'%(xk,self.cj[xk]))
    def getMaxFS(self):
        maxFS=[['',0]]
        for key in self.cj.keys():
            if self.cj[key]>maxFS[0][1]:
                maxFS=[]
                maxFS.append([key,self.cj[key]])
            elif self.cj[key]==maxFS[0][1]:
                maxFS.append([key,self.cj[key]])
        for myfs in maxFS:
            print('我的最好成绩是%s:%d'%(myfs[0],myfs[1]))
# class1=classes()
# joe=xs('joe','20',{'语文':69,'数学':80,'英语':100})
# joe.getXM()
# joe.getnl()
# joe.getcj('语文')
# joe.getMaxFS()
# print('---------------------')
# susan=xs('susan','20',{'语文':99,'数学':80,'英语':100})
# susan.getXM()
# susan.getnl()
# susan.getcj('语文')
# susan.getMaxFS()
# print('---------------------')
# class1.addPerson(joe)
# class1.addPerson(susan)
# class1.getRS()
a=...
print(a)