# for uname in ["a","b","c","d"]:
#     print(uname)
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     if letter in "BCDEFG":
#         print("a")
#     else:
#         print("b")
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# print("Type integers,each followed by Enter;or just Enter to finish")
# total=0
# count=0
# while True:
#     line=input("integer:")
#     if line:
#         try:
#             number =int(line)
#         except ValueError as err:
#                 print(err)
#                 continue
#                 total +=number
#                 count+=1
#     else:
#         break
#     if count:
#         print("count =",count,"total =",total,"mean =",total/count)

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# for i in range(1,11):
#     print(i)
# else:
#     print("The for loop is over")
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# print(random.randint(1, 10))  # 产生 1 到 10 的一个整数型随机数
# print(random.random())  # 产生 0 到 1 之间的随机浮点数
# print(random.uniform(1.1, 5.4))  # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
# print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数
#
# a = [1, 3, 5, 6, 7]  # 将序列a中的元素顺序打乱
# random.shuffle(a)
# print(a)
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# while True:
#     s=input("Enter something：")
#     if s=="quit":
#         break
#     if len(s)<3:
#         continue
#     print(s)
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# def printMax(a,b):
# #     if a>b:
# #         print(a,"    is maximum!")
# #     elif a<b:
# #         print(b,"    is maximum!")
# #     else:
# #         print ("xiangtong ")
# #
# #
# # printMax(7,5)
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# def func(x):
#     print("x is ",x)
#     x=2
#     print("Changed local x to ",x )
#
# x=50
# func(x)
# print("x is still ",x)
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# def say(message,times=1):
#         'aaaaaaaaaaaaaaaaa '
#         print(message*times)
#
# say("hello ")
# say("hello ",5)
# print(say.__doc__)
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# import sys
# print("The command line arguments are:")
# for i in sys.argv:
#     print(i)
# print("\n\nThe PYTHONPATH IS ",sys.path,"\n\n")

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# import mymodule
# mymodule.sayhi()
# print("Version",mymodule.modversion)

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #


# shoplist=['k','b','c','d','e','f','g']
# shoplist.sort(reverse=False)
# print(len(shoplist))
# for i in shoplist:
#     print(i)
#
# shoplist.reverse()
# print(len(shoplist))
# for i in shoplist:
#     print(i)
#
# shoplist.append('h')
# print(len(shoplist))

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #


# print("aaaaaaaaaaaaaaaaaaa\r\nbbbbbbbbbbbbbbbbbbb",file=open("C:/A.TXT","w"))


#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#
#   简单的电脑随机出题程序V1
#
#
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# num1=1
# num2=1
# babestr=""
# babeans=""
# i=1
# while i<=100:
#     num1 = random.randint(2, 100)
#     num2 = random.randint(1, 100)
#     babestr = babestr +"{:<10}\t\t\t\t".format( str(i) + ": " + str(num1) + "x" + str(num2)+"=")
#     babeans = babeans + "{:<10}\t\t\t\t".format(str(i) + ": " + str(num1 * num2) )
#     if i%4==0:
#         babestr=babestr+"\r\n"
#         babeans = babeans + "\r\n"
#     i=i+1
#
# print(babestr,file=open("C:/A.TXT","w"))
# print(babeans,file=open("C:/B.TXT","w"))

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# import  os
# import time
#
# temp_time=time.strftime("%Y%m%d")
# print(temp_time)
#
# help(int)
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def sayhello(self):
#         print("   "+self.name)
#
# p=Person("babe")
# p.sayhello()

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# class Person:
#     population=0
#     def __init__(self,name):
#         self.name=name
#         print("Initial    %s" %self.name)
#         Person.population+=1
#
#     def __del__(self):
#         print("_del_ ")
#         Person.population-=1
#         if(Person.population==1):
#             print("last one")
#         else:
#             print("There are still %d people left" %Person.population)
#
#
# p=Person("babe")
# p1=Person("babe1")
# p2=Person("babe2")
# p3=Person("babe3")

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#
# poem='''Programming is fun
#         When the work is done
#          if you wanna make your work also fun: use Python!'''
# with open("c:/poem.txt","w") as ff:
#     ff.write(poem)
#     ff.close()
#
# ab=open("c:/poem.txt","r")
#
# while True:
#     line=ab.readline()
#     )    if len(line)==0:
#         break
#     print(line)
# ab.close()
# print(poem


# import pickle
# shoplistfile="c:/shoplist.data"
# shoplist=["apple","mango","carrot","banana"]
# f=open(shoplistfile,'wb')
# pickle.dump(shoplist,f)
# f.close()
# del shoplist
# f=open(shoplistfile,'rb')
# storedlist=pickle.load(f)
# print(storedlist)

# import pickle
#
#
# a = {" name ","Tom", "age", "40"}
# with open('c:/text.data', 'wb') as file:
#      pickle.dump(a, file)
# with open('c:/text.data', 'rb') as file2:
#      b = pickle.load(file2)
#
# print(type(b))
# print(b)
# import os
# print("os.name"+os.name)
# print("os.getcwd()"+os.getcwd())
# # print("os.getenv()"+os.getenv())


# i=6
# j=7
# print("结果=",i,j,i,j,i,j)
# import random
# number=random.randint(1, 100)
# flag=True
#
# while flag:
#     guess=int(input("输入一个数字:"))
#     if guess==number:
#         print("答案正确，结束程序")
#         flag=False
#     elif guess<number:
#         print("数字小了")
#     else:
#         print("数字大了")
#
# def abc():
#     pass
# abc()

# list1 = ['Google', 'Runoob', 1997, 2000];
# list2 = [1, 2, 3, 4, 5, 6, 7];
#
# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])
#
# for x in [1, 2, 3]:
#     print(x,end="")

# mlist0=["1","2","3","4","5","6"]
# mlist1=mlist0;
# mlist2=mlist0[:]
# del mlist0[0]
# print("mlist0   ",mlist0)
# print("mlist1   ",mlist1)
# print("mlist2   ",mlist2)

# class SchoolMember:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("Initialized SchoolMemeber:%s",self.name)
#     def tell(self):
#         print("Name:%s Age:%s" %(self.name,self.age))
#
# class Teacher(SchoolMember):
#     def __init__(self,name,age,salary):
#         SchoolMember.__init__(self,name,age)
#         self.salary=salary
#         print("Initialized Teacher:%s",self.name)
#     def tell(self):
#         SchoolMember.tell(self)
#         print("Salary:%s" %self.salary)
#
# t=Teacher("Mrs.Shrividya",40,30000)
# print()
# t.tell()

# f=open("c:/A.TXT")
# while True:
#     line=f.readline()
#     if len(line)==0:
#         break
#     print(line,end="")
# f.close()

# mlist0=[1,2,3,4,5,6]
# print(sorted(mlist0))
# print(list(reversed(mlist0)))

# !/usr/bin/python3

# total = 0  # 这是一个全局变量
#
#
# # 可写函数说明
# def sum(arg1, arg2):
#     # global total
#
#
#     total = arg1 + arg2  # total在这里是局部变量.
#     print("函数内是局部变量 : ", total)
#     return total
#
# # 调用sum函数
# sum(10, 20)
# print("函数外是全局变量 : ", total)

# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

# 用户输入数字
# num1 = input('输入第一个数字：')
# num2 = input('输入第二个数字：')
#
# # 求和
# sum = float(num1) + float(num2)
#
# # 显示计算结果
# print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))

#
# num = 0
# while True:
#     num += 1
#     # 质数大于 1
#     if num > 1:
#         # 查看因子
#         for i in range(2, num):
#             if (num % i) == 0:
#                 #              print(num,"不是质数")
#                 #              print(i,"乘于",num//i,"是",num)
#                 break
#         else:
#             print(num, "是质数",end=" ")
#
#     # 如果输入的数字小于或等于 1，不是质数
#     else:
#         pass
# # print(num,"不是质数")
#
#     if num == 10000:
#         break

# import calendar
# monthRange = calendar.monthrange(2020,2)
# # calendar.
# print(monthRange[1])
# print(monthRange)
# print(calendar.mdays)

#
# people={}
# for x in range(1,31):
#     people[x]=1
# #print(people)
# check=0
# i=1
# j=0
# while i<=31:
#     if i == 31:
#         i=1
#     elif j == 15:
#         break
#     else:
#         if people[i] == 0:
#             i+=1
#             continue
#         else:
#             check+=1
#             if check ==7:
#                 people[i]=0
#                 check = 0
#                 print("{}号下船了".format(i))
#                 j+=1
#             else:
#                 i+=1
#                 continue

# def main():
#     fish = 1
#     while True:
#         total, enough = fish, True
#         for _ in range(5):
#             if (total - 1) % 5 == 0:
#                 total = (total - 1)  //  5 * 4
#             else:
#                 enough = False
#                 break
#         if enough:
#             print(f'总共有{fish}条鱼')
#             break
#         fish += 1


# # if __name__ == '__main__':
# main()

# motorcycles = ['honda', 'yamaha', 'suzuki'] 
# motorcycles.sort()
# print(motorcycles)
# motorcycles.sort(reverse=True)
# print(motorcycles)

# print(sorted(motorcycles))
# print(sorted(motorcycles,reverse=True))
# print(list(reversed(motorcycles)))

# motorcycles = ['honda', 'yamaha', 'suzuki'] 
# print(motorcycles[2])
# print(len(motorcycles))


# print(ord("好"))
# print(chr(22909))
# print(list(range(1,101)))
# print(list(range(1,101,2)))

# squares = [2**value for value in range(1,11)] 
# print(squares)
# l=list(range(1,1000001))
# print(sum(l))

# l1=[1,2,3,4,5]
# l2=l1[:]
# l3=l1
# l1.append(6)
# print(l2)
# print(l3)

# user_0 = { 'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }
# for key, value in user_0.items():
#     print("\nKey: " + key,end="   ") 
#     print("Value: " + value)

# favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', } 
# for name, language in favorite_languages.items(): 
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', } 
# for name in sorted(favorite_languages.keys()): 
#     print(name.title() + ", thank you for taking the poll.")

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = "" 
# while message != 'quit': 
#     message = input(prompt) 
#     print(message)

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
# print(pets) 
# while 'cat' in pets: 
#     pets.remove('cat') 
# print(pets)

# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """返回整洁的姓名"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# t='  '
# if t :
#     print("True")
# else:
#     print("Flase")

# def build_person(first_name, last_name):
#     """返回一个字典， 其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)

# def build_person(first_name, last_name, age=''):
#     """返回一个字典， 其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)


# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# # 这是一个无限循环!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# def greet_users(names):
#     """向列表中的每位用户都发出简单的问候"""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot',"a","b"]
# greet_users(usernames)

# # 首先创建一个列表， 其中包含一些要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # 模拟打印每个设计， 直到没有未打印的设计为止
# # 打印每个设计后， 都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     #模拟根据设计制作3D打印模型的过程
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
# # 显示打印好的所有模型
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     """
#     模拟打印每个设计， 直到没有未打印的设计为止
#     打印每个设计后， 都将其移到列表completed_models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

# def make_pizza(size, *toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a " + str(size) +
#     "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     """创建一个字典， 其中包含我们知道的有关用户的一切"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
# user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
# print(user_profile)


# class Dog():
#     """一次模拟小狗的简单尝试"""
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         print(self.name.title() + " is now sitting.")
#     def roll_over(self):
#         """模拟小狗被命令时打滚"""
#         print(self.name.title() + " rolled over!")

# my_dog = Dog('十一', 4)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
# my_dog.roll_over()
# print(my_dog.name)


# from collections import OrderedDict
# favorite_languages = OrderedDict()
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#     language.title() + ".")

# with open('c://A.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# with open('c://A.txt') as file_object:
#     for l in file_object:
#         # print(l,end="")
#         print(l,end="")


# with open('c://A.txt') as file_object:
#     lines=file_object.readlines()
#     for l in lines:
#         print(l,end="")


# t=time.gmtime()
# t=time.localtime()
# tt=datetime.datetime.now()

# print ('年：',t.tm_year)
# print ('月：',t.tm_mon)
# print ('日：',t.tm_mday)
# print ('小时：',t.tm_hour)
# print ('分钟',t.tm_min)
# print ('秒',t.tm_sec)
# # print ('毫秒',tt.microsecond)
# print ('星期：',t.tm_wday)
# print ('一年的第 %s 天' % t.tm_yday)
# print ('是否夏时令：',t.tm_isdst)
# print(time.strftime("%Y-%m-%d %H:%M:%S", t))


# print ('年：',tt.year)
# print ('月：',tt.month)
# print ('日：',tt.day)
# print ('小时：',tt.hour)
# print ('分钟',tt.month)
# print ('秒',tt.second)
# print ('毫秒',tt.microsecond)
# print ('星期：',tt.weekday())
# print ('一年的第 %s 天' % tt.strftime("%j"))
# print ('是否夏时令：',tt.dst())


# with open('c://tt.txt',"a") as file_object:
#   file_object.write(str(tt)+"\r\n")

# try:
#     i=1/0
# except :
#     print("error")
# else:
#     print("ok   "+str(i))


# def count_words(filename):
#     """计算一个文件大致包含多少个单词"""
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         # msg = "Sorry, the file " + filename + " does not exist."
#         # print(msg)
#         pass
#     else:
#         # 计算文件大致包含多少个单词
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) +
#         " words.")
# filename = 'c:/a.txt'
# # count_words(filename)

# filenames = ['c:/a.txt', 'c:/b.txt', 'c:/tt.txt', 'c:/little_women.txt']
# for filename in filenames:
#     count_words(filename)

# import json
# def get_stored_username():
#     """如果存储了用户名， 就获取它"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
# def get_new_username():
#     """提示用户输入用户名"""
#     username = input("What is your name? ")
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#     return username
#
# def greet_user():
#     """问候用户， 并指出其名字"""
#     username = get_stored_username()
#     if username:
#         print("Welcome back, " + username + "!")
#     else:
#         username = get_new_username()
#         print("We'll remember you when you come back, " + username + "!")
#
# greet_user()
# print(round(random.uniform(0,100),2))

# import  random
#
# print(round(random.uniform(0,100),2))

# n = input("enter a number to process: ")
# n = int(n)
# if n >= 10:
#     for i in range(1, n + 1):
#         print(i)

# print('G' > 'g')
# lang="Python"
# print(lang[:-6])

# print([[x, x + 1, x + 2] for x in range(0, 3)])
#
# a = 5
# b = 6
# c = a if a > b else b
#
# print(c)

#
# if 'a':
#     print("True")
# else:
#     print("False")

# color = ['Red', 'Green', 'Blue']
# R, G, B = color
# print(G)
#
# score = 50 > 35
# print("Pass" if score else "Fail")

# import operator as op
#
# print(op.truediv(1231, 17))
# print(op.add(123, 456))

# a = 'asdfghjkl'
# print(a[1:].startswith('s'))

# lang = 'Python'
# print('=' * 21)
# print(*lang, sep='|')
# print('-' * 21)
# print(*range(len(lang)), sep='|')
# print('=' * 21)

# t = 'abcbbbbbbbbbbbbd'
# print(t.center(20, "!"))
# print(t.count("b", 0, 5))

# s = ''
# print(True if s else False)
#
#
# def myFunc(n):
#     if n == 0:
#         return 0
#     else:
#         return n + myFunc(n - 1)
#
#
# print(myFunc(5))

# for i in range(6):
#     i += i
# else:
#     print(i)
#
# print(sum([1, 2], 7))
#
#
#
#
# class A:
#     def __init__(self):
#         self.__name = 'Micheal'
#
#
# abc = A()
# print(abc.__name)


a = {'b': 'c', 'c': 'd', 'd': 'b'}
b = a[a['b']]
print(a[b])

dic = {"a": 2, "a": 3}
n = dic["a"]
print(n)

name = 'Mari Muthu'
print(name.rfind('M'))


def prt():
    name = 'Brisa'
    company = (lambda x: name + '' + x)
    return company


my_prt = prt()
print(my_prt('Technologies'))
