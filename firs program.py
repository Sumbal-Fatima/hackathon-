# a=2
# b=3
# sum=a+b
# print(sum)
# print(a%b)
# print(a**b)
# a= int (input("enter side a", ))
# b= int (input("enter side b", ))
# print(a*b)
# print (type(a))
# age = 75 

# if(age <= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

# num = int(input("enter a number= "))

# if(num % 2 == 0):
#     print("EVEN")
# else:
#     print("ODD")
# a = 4
# b = 5
# c = 7 
# d = 9
# if(a>b and a>c and a>d):
#     print("greater number= A")
# elif(b>c and b>a and b>d):
#     print("greater number= B")
# elif(c>a and c>b and c>d):
#     print("greater number= C")
# else:
#     print("greater number= D")
# num = int(input("enter a number", ))
# if(num % 7 == 0 ):
#     print("num is multiple of 7")
# else:
#     print("not multiple of 7")
# str=  "my name is sumbal"
# print((str.replace("sumbal", "muhammad")))
# movies = ["dil waly, jab we met , hero panti"]
# print(type(movies))
# print(movies)
# movies = ['jab we met', 'love life', 'hero panti']
# # movie1 = (input("enter 1st movie", ))
# # movie2= (input("enter 2nd movie", ))
# # movie3 = (input("enter 3rd movie", ))
# # movies.append(movie1)
# # movies.append(movie2)
# # movies.append(movie3)
# movies.insert(0,helo)
# print(movies)
# list = [1,2,3,4]
# list.insert(2, 3)
# print(list)
# list.remove(3)
# print(list)
# list.pop(3)
# print(list)
# tup =["C","D","A", "A", "B", "B", "A"]
# tup.sort()
# print(tup)
# name= "$sumbal$ $fatima$"
# print(name.count("
# a = int(input("enter a number:" ))
# # b =int((input"enter a number:" ))
# # c = int((input"enter a number:" ))
# if(a % 2== 0):
#     print("EVEN")
# else:
#     print("ODD")
# info = {
#     "sumbal" : "awais",
#     "muhammad" : "ali",
#     "fatima" : "hassan",
#     "hussain" : "maryam",
#     "subject" : {
#         "python" : 40,
#         "c" : 30,
#         "java" : 60,
#     },
#     "topic" : ("set","dictionary"),
# }
# # print(len(list(info.keys())))
# # print(list(info.values()))
# # pairs = (list(info.items()))
# # print(pairs[0])
# # dict = {
# #     "table" : ["a piece of furniture", "list of  facts and figures"], 
# #     "cat" : "a small animal"

# # }
# # print(dict["table"])
# # set = {"python", "java", "c++", "python", "java", "c++","python", "java", "c","javascript"}
# # print(len(set))
# null_dict = {}
# marks = int(input("enter phy :" )) 
# null_dict.update({"phy" : marks })

# marks = int(input("enter chem :" ))
# null_dict.update({"chem" : marks })

# marks = int(input("enter math :" ))
# null_dict.update({"math" : marks })
# print(null_dict)

# i = 10
# while i:
#     i >= 1
    # print(i)
# f = open("practice.txt", "a")
# f.write("\n hi i love my family")


# f = open("practice.txt", "r")
# data = f.read()
# print(data)

# f = open("sample.txt", "w+")

# print(f.read())
# f.write("bye")
# f.close()

# f = open("sample.txt", "r")
# data = f.read()
# print(data)
# with open("practice.txt","r") as f:
#     f.read()
#     print(f.read())

# class 8

# class Student:
    
#     def __init__(self):
        
        
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        

# s1 = Student("karan", 97)
# print(s1.name, s1.marks)

# s2 = Student("arjun", 98)
# print(s2.name, s2.marks)

# class Car:
#     color = "blue"
#     brand = "marcedes"
# car1 = Car()
# print(car1.color.brand)

# class Student:
    
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg score is:", sum/3)

# s1 = Student("sumbal", [97,98,99])
# s1.get_avg()
# s1.name = "fatima"
# s1.get_avg()





# 
# f = open("practice.txt","a")
# f.write("\nthen i move to usa")
# f.close()
# f = open("demo.txt","a+")
# f.write("heloo mrs")
# print(f.read())
# f.close()
# import os
# os.remove("practice.txt")


# class Student:
    
        
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def welcome(self):
#         print("welcome student,", self.name)
#     def get_marks(self):
#         print(self.marks)
        

# s1 = Student("karan", 97)
# print(s1.name, s1.marks)
# s1.welcome()
# s1.get_marks()

# s2 = Student("arjun", 98)
# print(s2.name, s2.marks)
# s2.welcome()
# s2.get_marks()

# class Student:

#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks 
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avge score is:", sum/3)

# s1 = Student("tony stark", [91, 98, 99])
# s1.get_avg()
        

# class Account: 
#     def __int__(self, bal, acc):
#         self.balance = bal 
#         self.account_no = acc
#     def debit(self, amount):
#         self.balance -= amount 
#         print("rs", amount, "was debited")
#         print("total balance", self.get_balance())
#     def credit(self, amount):
#         self.balance += amount
#         print("rs", amount, "was credited")
#         print("total balance", self.get_balance())
#     def get_balance(self):
#         return self.balance
# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# class Account:
#     def __init__(self, accno, accpass):
#         self.accno = accno
#         self.__accpass = accpass
#     def resetpass(self):
#         print(self.__accpass)
        

# acc1 = Account(1234, 4567)
# print(acc1.accno)
# acc1.resetpass()
# class Person:
#     name = "sumbal"
#     def __hello(self):
#         print("helo person")
#     def welcome(self):
#         (self.__hello())
# p1 = Person()
# (p1.welcome())

# multi level
# class Cars:
#     @staticmethod
#     def strt():
#         print("car start")
#     @staticmethod
#     def stop():
#         print("car stop")
# class Toyotacar(Cars):
#     def __init__(self, brand):
#         self.brand = brand
# class fortuner(Toyotacar):
#     def __init__(self, type, brand):
#         self.type = type
#         super().__init__(brand)
# cr1 = fortuner("diesel","local")
# cr1.strt()
# print(cr1.brand)
# print(cr1.type)

# multiple INHERITENSE
# class A:
#     varA = "welcome to class A" 
# class B:
#     varB = "welcome to class B" 
# class C(A,B):
#     varC = "welcome to class C" 
# c1 = C()
# print(c1.varA, c1.varB, c1.varC)
# class Cars:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def strt():
#         print("car start")
#     @staticmethod
#     def stop():
#         print("car stop")
# class Toyotacar(Cars):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)

# c1 = Toyotacar("marcedes", "electric")
# print(c1.type)
# print(c1.name)

# # class fortuner(Toyotacar):
# #     def __init__(self, type):
# #         self.type = type

# # cr1 = fortuner("diesel")
# # cr1.strt()
# # print(cr1.brand)

# class Person:
#     name = "sumbal"
#     def changename(self, name):
#         self.name = name
# s1 = Person()
# s1.changename("muhammad")
# print(s1.name)
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentange = str((self.phy + self.chem + self.math)/3) + "%"

# s1 = Student(98, 97, 99)
# print(s1.percentange)
# class Employ:
#     def __init__(self, role, dpt, salary):
#         self.role = role 
#         self.dpt = dpt 
#         self. salary = salary 
#     def showdettails(self):
#         print("role =", self.role)
#         print("dpt =", self.dpt)
#         print("salary =", self.salary)

# class Engineer(Employ):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
#         super().__init__("Engineer", "water", "60000")
# e1 = Engineer("sumbal", 23)
# print(e1.name)
# print(e1.age)
# e1.showdettails()
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#     def __gt__(self, or2):
#         return self.price > or2.price

# or1 = Order("chips", 100)
# or2 = Order("drink", 90)

# print(or1 > or2)
