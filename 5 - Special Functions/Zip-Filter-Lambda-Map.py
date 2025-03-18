#ZIP

l1 = ['A','B','C']
l2 = [1,2,3]
print(zip(l1,l2))
print(list(zip(l1,l2)))
print('-'*21)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(list(zip(matrix)))
print([list(row) for row in zip(matrix)])
#transpose
print([list(row) for row in zip(*matrix)])
#double-transpose
print([list(row) for row in zip(*[list(row) for row in zip(*matrix)])])
print('-'*21)

lst1 = [2,4,6]
lst2 = [1,3,5]
print(sum([i*j for i,j in zip(lst1,lst2)]))
print('-'*21)

#Filter

lst = [1,2,3,4,5,6,7,8,9,0]
def is_even(n):
    return n%2==0
print(list(filter(is_even,lst)))
print('-'*21)
#Lambda

add_num = lambda x,y: x*y
print(add_num(5,10))
print('-'*21)

print(list(filter(lambda x: x%2==0,lst)))
print('-'*21)

#MAP
def sqr(x):
    return x**2
print(list(map(lambda x: x**2 ,lst)))
print('-'*21)

names = ['akash','kirti','sreyanshu','swosti']
print(list(map(lambda x: len(x),names)))




