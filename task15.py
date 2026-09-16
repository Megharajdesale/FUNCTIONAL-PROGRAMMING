#nested function  
# Three Nested Function.

def outer_fun():
    print("We are the inside outer function")
    def inner_fun():
        print("We are the inside inner function")
        def supper_inner_fun():
            print("We are a inside supper inner function")
            

        return supper_inner_fun
    return inner_fun
inner_fun = outer_fun()
supper_inner_fun = inner_fun()
supper_inner_fun()
print(supper_inner_fun)

#o/p--> We are the inside outer function
#       We are the inside inner function
#       We are a inside supper inner function
#       <function outer_fun.<locals>.inner_fun.<locals>.supper_inner_fun at 0x00000185DAE03740>


#Four Nested function.
def outer_fun():
    print("We are the inside outer function")
    def inner_fun():
        print("We are the inside inner function")
        def supper_inner_fun():
            print("We are the inside supper inner function")
            def most_inner_fun():
                print("We are the inside most inner function")

            return most_inner_fun
        return supper_inner_fun
    return inner_fun
inner_fun = outer_fun()
supper_inner_fun = inner_fun()
most_inner_fun = supper_inner_fun()
most_inner_fun()
print(most_inner_fun)

#o/p--> We are the inside outer function
#       We are the inside inner function
#       We are the inside supper inner function
#       We are the inside most inner function
#      <function outer_fun.<locals>.inner_fun.<locals>.supper_inner_fun.<locals>.most_inner_fun at 0x0000028ADD5737F0>



# task<1>Write three nested functions — outer_fun, inner_fun, and 
# super_inner_fun — that take one number each (a, b, c) and return 
# their sum, using closures. Also verify the types of intermediate results 
# (function objects) vs the final result (int).

def outer_fun(a):
    def inner_fun(b):
        def supper_inner_fun(c):
            return a + b + c
        return supper_inner_fun
    return inner_fun
result = outer_fun(10)(20)(30)
print(result)

print(type(outer_fun(10)))
print(type(outer_fun(10)(20)))
print(type(outer_fun(10)(20)(30)))

#o/p--> 60
#          <class 'function'>
#          <class 'function'>
#          <class 'int'>