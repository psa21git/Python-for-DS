dct = {
    1: {
        'name' : 'Abhijeet',
        'phone' : 29137
    },
    2: {
        'name': 'Abhisek',
        'phone': 21341
    }
}
print(dct)
print('-'*21)

print(dct[1]['name'])
print('-'*21)

for key in dct.keys():
    print(key,dct[key]['name'])
print('-'*21)

# a level deeper
data = {
    1: {
        'name' : 'Abhijeet',
        'phone' : 29137,
        'marks':{
            'math':70,
            'DAA':60
        }
    },
    2: {
        'name': 'Abhisek',
        'phone': 21341,
        'marks':{
            'math':67,
            'DAA':69
        }
    }
}

for k in data.keys():
    print(f'DAA marks of {data[k]['name']} => {data[k]['marks']['DAA']}/80')

print('-'*21)