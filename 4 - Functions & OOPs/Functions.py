def greet():
    print("Hello")

greet()
print('-'*21)
print([greet() for i in range(5)])
# None is stored 5 times as this function doesnot return anything
print('-'*21)

global_var = 10
def scope():
    local_var = 5
    print(global_var,local_var)
# print(global_var,local_var)
scope()
print('-'*21)

def greet(name="$$$$"):
    print("hello ",name)
greet("Priyanka")
greet(name="PSA")
greet()
print('-'*21)


def add(a=0,b=0):
    # print(f"{a} + {b} = {a+b}")
    return a+b
add(b=23,a=56)
print(greet(),"-> returned from greet() func")
var = add(21)
print(var)
print('-'*21)

def arithmetic(a=10,b=10):
    return a+b,a-b,a*b,a/b
print(arithmetic(3))
print('-'*21)

lst = [1,2,3,4,5]
def sq(lst):
    return [i**2 for i in lst]
def cub(lst):
    return [i**3 for i in lst]
def final_sum(lst):
    return [sq(lst)[i]+cub(lst)[i] for i in range(len(lst))]
print(final_sum(lst))
print('-'*21)