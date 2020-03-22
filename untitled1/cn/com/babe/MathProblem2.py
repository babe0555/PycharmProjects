# -*-coding:utf-8-*-
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#
#   简单的电脑随机出题程序V2
#
#
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #


import random
'''

简单的电脑随机出题程序V2

'''

mathlist=[]
resultlist=[]


#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机批量产生加法题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#               tot_num 出题总数
#               通过调用addnum（）函数，把题和答案分别存在在mathlist resultlist 集合中
#
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def add_amount(num1=1,num2=1,tot_num=1):
    i=1
    while i<=tot_num:
        ls=addnum(num1,num2)
        mathlist.append(ls[0])
        resultlist.append(ls[1])
        i=i+1

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机产生加法题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#
#
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def addfloat(num1=1,num2=1):
    returnlist=[]
    # n1=random.randint(1, num1)
    n1=random.uniform(0,num1)
    # n2=random.randint(1, num2)
    n2=random.uniform(0,num2)

    returnstr = str(n1) + "＋" + str(n2) + "="

    returnans=n1+n2
    returnlist.append(returnstr)
    returnlist.append(returnans)
    return returnlist

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机批量产生减法题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#               tot_num 出题总数
#               通过调用sub（）函数，把题和答案分别存在在mathlist resultlist 集合中
#               flag=0，那被减数必须大于减数  flag=其他数  被减数可以小于减数
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def sub_amount(num1=1,num2=1,tot_num=1,flag=0):
    i=1
    while i<=tot_num:
        ls=sub(num1,num2,flag)
        mathlist.append(ls[0])
        resultlist.append(ls[1])
        i=i+1

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机产生减法题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#               随机生成的被减数必须要大于减数
#               flag=0，那被减数必须大于减数  flag=其他数  被减数可以小于减数
#
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def sub(num1=1,num2=1,flag=0):
    returnlist=[]
    returnstr=""
    returnans=0
    if flag==0:
        while True:
            n1=random.randint(1, num1)
            n2=random.randint(1, num2)
            if(n1>n2):
                returnstr = str(n1) + "－" + str(n2) + "="
                returnans = n1 - n2
                break
    else:
        n1 = random.randint(1, num1)
        n2 = random.randint(1, num2)
        returnstr = str(n1) + "-" + str(n2) + "="
        returnans = n1 - n2

    returnlist.append(returnstr)
    returnlist.append(returnans)
    return returnlist

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机批量产生乘法题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#               tot_num 出题总数
#               通过调用sub（）函数，把题和答案分别存在在mathlist resultlist 集合中
#               flag=0，那被减数必须大于减数  flag=其他数  被减数可以小于减数
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def mul_amount(num1=1,num2=1,tot_num=1):
    i=1
    while i<=tot_num:
        ls=mul(num1,num2)
        mathlist.append(ls[0])
        resultlist.append(ls[1])
        i=i+1

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机产生乘法题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#               随机生成的被减数必须要大于减数
#
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def mul(num1=1,num2=1):
    returnlist=[]
    returnstr=""
    returnans=0
    n1 = random.randint(1, num1)
    n2 = random.randint(1, num2)
    returnstr = str(n1) + "×" + str(n2) + "="
    returnans = n1 * n2

    returnlist.append(returnstr)
    returnlist.append(returnans)
    return returnlist

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机批量产生除法题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#               tot_num 出题总数
#               通过调用sub（）函数，把题和答案分别存在在mathlist resultlist 集合中
#               flag=0，那被减数必须大于减数  flag=其他数  被减数可以小于减数
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def div_amount(num1=1,num2=1,tot_num=1):
    i=1
    while i<=tot_num:
        ls=div(num1,num2)
        mathlist.append(ls[0])
        resultlist.append(ls[1])
        i=i+1

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机产生除法题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#               随机生成的被减数必须要大于减数
#
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def div(num1=1,num2=1):
    returnlist=[]
    returnstr=""
    returnans=0
    while True:
        n1 = random.randint(1, num1)
        n2 = random.randint(1, num2)
        if (n1 > n2):
            returnstr = str(n1) + "÷" + str(n2) + "="
            if(n1%n2!=0):
                returnans = str(n1 // n2)+"~"+str(n1%n2)
            else:
                returnans = str(n1 // n2)
            break
    returnlist.append(returnstr)
    returnlist.append(returnans)
    return returnlist

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               随机产生数学题
#               num1    第一个最大随机数
#               num2    第二个最大随机数
#               tot_num 出题总数
#               flag=0，那被减数必须大于减数  flag=其他数  被减数可以小于减数
#
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def ran_amount(num1=1,num2=1,tot_num=1,subflag=0):
    i = 1
    while i <= tot_num:
        fl=random.randint(1, 2)
        if fl==1:
            ls = addnum(num1, num2)
        elif fl==2:
            ls=sub(num1, num2,subflag)
        elif fl==3:
            ls =mul(num1, num2)
        elif fl==4:
            ls=div(num1, num2)

        mathlist.append(ls[0])
        resultlist.append(ls[1])
        i = i + 1

#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#               输入打印
#               flag 0加法 1减法 2乘法 3除法 4随机
#               num2    第二个最大随机数
#               随机生成的被减数必须要大于减数
#
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
def outTxt(flag=0,num1=1,num2=1,amount=1):
    outstr=""
    outans=""
    if flag==0:
        add_amount(num1,num2,amount)
    elif flag==1:
        sub_amount(num1,num2,amount)
    elif flag==2:
        mul_amount(num1,num2,amount)
    elif flag==3:
        div_amount(num1, num2, amount)
    elif flag==4:
        ran_amount(num1, num2, amount)



    for index in range(len(mathlist)):
        outstr=outstr+"{:<21}".format(str(index+1)+"："+str(mathlist[index]))
        outans=outans+"{:<21}".format(str(index+1)+"："+str(resultlist[index]))
        if((index+1)%4==0 and index!=0):
            outstr = outstr + "\r\n"
            outans = outans + "\r\n"

    print(outstr,file=open("C:/A.TXT","w"))
    print(outans,file=open("C:/B.TXT","w"))



#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#           测试部分
#  #  #   #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# ls=add_amount(1000,1000,10)
# print(str(ls[0])+""+str(ls[1]))
# div_amount(1000,100,10)
# indexi=mathlist.__len__()
# i=0
# while i<indexi:
#     print(str(mathlist[i])+""+str(resultlist[i]))
#     i=i+1
#
# for index in range(len(mathlist)):
#     print(str(mathlist[index])+""+str(resultlist[index]))

outTxt(4,9000,8000,30)
