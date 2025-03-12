lst = ['Asish','Nitish','Manini','PSA']
print(lst)
print(lst[-3])
print('-'*20)

#Modify the values
lst[2] = 'Sansa'
print(lst)
# print('-'*20)

#length of a list
print("Length of list is ",len(lst))
print('-'*20)

#Slicing
print(lst[1:3])
print('-'*20)

#Reverse ?
print(lst[::-1])
print(lst[::-2])
lst.reverse()
print(lst)
print('-'*20)

#Appending & Removing
lst.append("Ritesh")
print(lst)
lst.remove('Sansa')
print(lst)
print('-'*20)

#Sorting a List
l = [3,53,62,13,34,89,2,35,99]
print(sorted(l))
print("Descending Sort ->")
l.sort(reverse=True)
print(l)
print('-'*20)

#Finding an element
print("PSA is at ",lst.index('PSA'))

#COunt
print(lst.count('PSA'))
print('-'*20)

#Delete an element using INdex
print(lst)
del lst[2]
print(lst)
print('-'*20)

#Extend
lst.extend(['Amulya','Jahnvi','Kendall'])
print(lst)
print('-'*20)

#Maximum and Minimum
print("max is ",max(l))
print('min is ',min(l))
print('-'*20)

#Iterating through an list | Direct
for i in lst:
    print(i)
print('-'*20)

#Iterating through an list | Indexing
for i in range(len(lst)):
    print(i,lst[i])
print('-'*20)

#Iterating through an list | Reverse
for i in range(len(lst)-1,-1,-1):
    print(i,lst[i])
print('-'*20)


