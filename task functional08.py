# pattern printing using functional.

# write a program to create square pattern.
def square_pattern ():  # function start
    for row in range(0 ,5):
        for col in range(0 , 5):
            print("*" , end=' ')
        print()
square_pattern()  #function call

# output-- >
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

#task <2> write  program to right angal triagal number pattern.
def right_angal_triagal_number():   #function start
    for row in range(0 , 5):
        for col in range(0 , row+1):
            print(col+1 , end=' ')
        print()
right_angal_triagal_number() #function call

#output-->
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

#<3> task.  wap to inverted right angal traingal number pattern.
def invated_right_angal():
    for row in range(0 , 5):
        for col in range(row , 5):
            print(col +1 , end = ' ')
        print()
invated_right_angal()


#output-->
# 1 2 3 4 5 
# 2 3 4 5 
# 3 4 5 
# 4 5 
# 5 


#<4> write a program diamond star pattern using functional.
def diamond_star(): #function start
    n = eval(input("Enter a number of row :"))
    #upper half (expanding)
    for i in range(1 , n +1):
        for s in range(1 , n -i +1):
            print(" " , end=" ")
        for k in range(1 , 2*i):
            print("*" , end=" ")
        print()

    #lower half(constarcting)
    for i in range(n -1 , 0 ,-1):
        for s in range(1 , n -i +1):
            print(" " , end=" ")
        for k in range(1 , 2 *i):
            print("*" , end=" ")
        print()

diamond_star()     #function call

#output--> 
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

#<5> task.piramid pattern: print a symetric pyramid of * with n rows, centered using a spaces.
def piramid_star_pattern():
    n = eval(input("Enter a number of rows :"))
    for i in range(1 , n +1):
        for s in range(1 , n-i +1):
            print(" " , end=" ")
        for k in range(1 , 2 *i):
            print("*" , end=" ")
        print()
piramid_star_pattern()
#output-->
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

#<6> task.Floyd's Triangle: Print continuous numbers in a right-triangle shape without resetting each row.
def floyd_triangal():
    n = eval(input("Enter number of row :"))
    num =1
    for i in range(1 , n +1):
        for k in range(1 , i +1):
            print(num , end= " ")
            num +=1
        print()
floyd_triangal()
#output-->
# Enter number of row :4
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 


#<7> task. #Hollow Square Pattern: Write a program that takes an integer n as input
#  and prints a square of * where only the border (first row, last row, first column, last column)
#  is filled with stars, and the inside is empty (space).
def hollow_square_pattern():
    n = int(input("enter number of rows: ")) #n=5
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or i == n or j == 1 or j == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()    
hollow_square_pattern()

#output-->
# enter number of rows: 5
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * * 

