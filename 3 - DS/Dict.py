# key:value
# key must be unique
# dict[key] = value

dict = {
    1:"Asish",
    2:"Ankur",
    3:"Avneet",
    1:"Sakshi" #if key is overriden then last value is only present
}

print(dict)
print('-'*21)
print(dict[1])
print(dict.get(3))
print('-'*21)

#adding a new pair
dict[7] = 'CR'
print(dict[7])
dict[7] = 'MSD'
print(dict[7])
del dict[7]
print(dict)
print('-'*21)

#Iterating
print(dict.keys())
print(dict.values())
print('-'*21)

for i in dict.keys():
    print(i,dict[i])
print('-'*21)

print(dict.items())
for i in dict.items():
    print(i[0],i[1])
print('-'*21)
for i,j in dict.items():
    print(i,j)
print('-'*21)

#check if key is present
print(1 in dict)
print('1' in dict)
print('-'*21)

#updating/merge? two dictionaries
dict1 = {
    1:'A',
    2:'B',
    4:'D'
}
dict2 = {
    1:'a',
    2:'b',
    3:'c'
}
dict1.update(dict2)
print(f'dict1 = {dict1}')
print(f'dict2 = {dict2}')
print('-'*21)

