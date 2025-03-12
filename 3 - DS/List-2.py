#MultiDimensional Lists!

lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(lst)
print(lst[2])
print(lst[0][2])
print('-'*20)

#all functions are similar to what we did in 1D lists

#Multi-Dimensional Matrix
for i in lst:
    for j in i:
        print(lst.index(i),i.index(j),' = ',j)
print('-'*20)
