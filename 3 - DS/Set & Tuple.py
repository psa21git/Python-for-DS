#Sets are mutable / Tuples are immutable

myset = {1,2,3,4,5}
print(myset)
print(type(myset))
print('-'*21)

#add
myset.add(6)
print(myset)
print('-'*21)

#pop
print(myset)
poppi = myset.pop()
print(poppi)
print('-'*21)

#remove
print(myset)
myset.discard(4)
print(myset)
print('-'*21)

#Iteration is same and simple as lists

print(2 in myset)
print(21 in myset)
print('-'*21)

#SET Ops
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1)
print(set2)
print('Union : ',set1 | set2)
print('Intersection : ',set1 & set2)
print('Difference : ',set1 - set2)
print('Difference : ',set2 - set1)
print('Symmetric Difference : ',set2 ^ set1)
print('-'*21)

#Clear
print(myset)
myset.clear()
print(myset)
print('-'*21)

# TUPLEEEE
# max things are similar to what we know !

tup1 = (1,2,3,4,5)
tup2 = (4,5,6,7,8)
print(tup1 + tup2) #concatenation
print('-'*21)

tup = tup1 + tup2
print(tup.count(4))
print('-'*21)

