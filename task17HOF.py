#1> Addition

from functools import reduce
def add_two(n1, n2):
    return n1 + n2
l = [1,2,3,4,5,6]
res = reduce(add_two,l)
print(res)       #OP:-21


#2> subtraction

from functools import reduce
def sub_two(n1, n2):
    return n1 - n2
l = [1,2,3,4,5,6]
res = reduce(sub_two,l)
print(res)   #OP:-  -19

#3> multiplication

from functools import reduce
def mult_two(n1, n2):
    return n1 * n2
l = [1,2,3,4,5,6]
res = reduce(mult_two,l)
print(res)   #OP:-  720

#4> maximum

from functools import reduce
def find_max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
l = [1,2,3,4,5,6]
res = reduce(find_max,l)
print(res)   #OP:- 6

#5> minimum

from functools import reduce
def find_min(n1, n2):
    if n1 < n2 :
        return n1
    else:
        return n2
l = [1,2,3,4,5,6]
res = reduce(find_min,l)
print(res)    #OP:- 1





#Q How to find even number list

# def f1(even) -> bool:
#     return even % 2 ==0
    
# def f2(odd):
#     return odd % 2 == 1
# def my_HOF(f,l):
#     new_list = []
#     for i in l:
#         if f2(i):
#             new_list.append(i)
#     return new_list    

# lst  = [1,2,3,4,5,6]
# # even_list = my_HOF(f1,lst)
# odd_list = my_HOF(f2,lst)
# print(f"original list : {lst}")
# # print(f"even list : {even_list}")
# print(f"odd list : {odd_list}")



