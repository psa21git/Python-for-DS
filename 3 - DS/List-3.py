#Square all the elements
lst = [1,2,3,4,5,6,7]
print(lst)
lst = [i**2 for i in lst]
print(lst)
print('-'*20)

#Finding first 10 even numbers
lst = [i for i in range(20) if i%2==0]
print(lst)
print('-'*20)

#maths table of user choice
# n = int(input('enter a number : '))
# lst = [i for i in range(n,n*10+1,n)]
# print(lst)
# print('-'*20)

#multi-dimensional
#this concept is still not clear in MultiDimensional
#How to create a list of [[1,2],[3,4]] using comprehension ?
print([[i for i in range(2)] for j in range(3)])
print('-'*20)
print([[i for i in range(3)] for j in range(3)])
print('-'*20)

print([[x,x+1,x+2] for x in range(1,9,3)])