#List Comprehensions

dct = {i:i**2 for i in range(1,11) if i%2==1}
print(dct)
print('-'*21)

#Dicts from lists
l = ['Apple','Orange','Grapes']
d = {item:len(item) for item in l}
print(d)
print('-'*21)

#Special Keys with Strings
dict = {f'num_{i}':i for i in range(1,101)}
print(dict)
print('-'*21)

dict7 = {k:v for k,v in dict.items() if v%7==0}
print(dict7)
print('-'*21)

lst1 = [1,2,3]
lst2 = ['one','two','three']
dict_list = {lst1[i]:lst2[i] for i in range(len(lst2))}
print(dict_list)
print('-'*21)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
dict_matrix = {(i,j):matrix[i][j] for i in range(3) for j in range(3)}
print(dict_matrix)
print('-'*21)