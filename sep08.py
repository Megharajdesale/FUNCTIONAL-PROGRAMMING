#----->FUNCTIONAL PROGRAMMING  <----#
# Introduction
# Function definition
# Function calling

#--->Type of programming.

# 1> Sequential / procedural
# 2> Functinal
# 3> Object Oriented Proframming

# <1>sequential.
# a = 10
# print(10)
# for i in a:
#     print(i)
# that type of called sequential programming.



#  Q what is function ?
#--> function is subprogarm , bunch of code or group or code stetments that
#parform a specific task.

#  .function will exequte only when it is called / invoked.

#. After executing the function it will return a value to the caller.

# <Q> There era two types of functions in python:
# <1> Built in function -->
#         ---> These are the function which are already defined in python.
#       len , input , print , range , sum , min , max , enumarate , int , 
#       float , bin , oct , hex , str, etc.  
# 
#  <2> User defined functions :-->
#     ----> These are the functions which are defined by the user.
# *myprint,atuls_sir_max
# 
# <**> There two IMP things in Functional Programming :
# <1> Function defined :---> it is the process of creating a function.
# 
# <2> Function call : --> it is the process of invoking function.
  
# <Q> How to define function in python ?
#---> By using 'def' keywords we can define a function in python.

#<*> Syntax-->
# ---> def function_name(input_parametere)   #start of afunction.
#           function body
#               pass           #it is reseved in future


# <Q> How two call a function in python ? 
# ----> By using function name and passing the required input parameters
#       we can call a function in python.

#<*> Syntax-->
#     --->     function_name(input_aargument)        #function call


#<Q> What is parametere ?
#--> A Parametere is a variable listed in a function / method's definitioans
#   its a placehilder that receives a value when the function is called.

#<Q> What is aargument ?
#--> An argument is the actual value you pass to a function when you call it.
#   when it assigned to the function's parametere.

#<Q> Differance between parametere and aargument ?
# ---> A Parametere is the variable listed in afunction's definition's,
#      while an argument is the actual value passed to the function 
#      when it is called.

#<Q> Create a function  to add two numbers and print the result.

# print("start of the program")
# function definition 
# def add_two_numbers():
#     print("we are inside the function add-two_numbers")
#     a = 10
#     b = 20
#     print(f"the sum of {a} and {b} is : {a+b}")
#     print("end of the function add_two_numbers")
# print("we are calling the function add_two_numbers")
# add_two_numbers()   # Function call
# print("we are check to the main program after execution the function add_two_numbers")
# print("end of the program")

#output-->PS C:\batch 1341 WS\core python work space\functinal ws> py sep08.py                                                         
# start of the program                                                   
# we are calling the function add_two_numbers
# we are inside the function add-two_numbers
# the sum of 10 and 20 is : 30
# end of the function add_two_numbers
# we are check to the main program after execution the function add_two_numbers
# end of the program

#<Q> create a code Dinamic ?
# print("start of the program")
# def add_tow_numbers():
#     print("we are inside the functions add_two_numbers")
#     a = eval(input("enter a first number :"))
#     b = eval(input("enter a second number :")) 
#     print(f"the sum of {a} and {b} is : {a+b}")
#     print("end of the function add_two_numbers")
# print("we are calling function add_two_numbers")
# add_tow_numbers()                          #function call
# print("we are back two the main program after executing the function add_two_numbers")
# print("end of the program") 

#<Q> Write a program check wether given number even or odd.

     #function call


#<Q> After exequting a function it will return a value the caller ?
# value = check_even_odd()   #function call
# print(f"the return value of the function check_even_or_odd is : {value}")

#---> by defualt python functoin will return 'none' if we dont's specify any return value in the functoin.

#<Q> interview quastion on the belowe code.
# what will happend and what will return ?
# result = print("Hello")
# print(result) 
# output-->Hello
#          None   #print function it is always return thr none data type.


#<Q> why return inpute function after executing ?
# r1 = input()
# print(type(r1))
#output--> <'class' , 'str'>  #any function is always return the different data type, like (str,tuple,list,etc)

#<Q> machin test quastion .
# that code execute,how will return after execution on display?
# r1 = print("Hello")
# r2 = print(r1)
# r3 = print(r2)
# print(r3)
#output-- > HEllo
#           None
#           None
#           None


#<Q> in IT indrustry interviewer ask that same quastion in this type.
# print(print(print(print("Hello"))))

#option:->
# A> Hello None None Hello
# B> None None Hello Hello
# C> None None None Hello
# D> Hello None None None   #(corect answer (D))
# E> Hello Hello Hello Hello 

  



     

