#MATH
import math

x = 10.8
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print('-'*21)

y = 3
print(math.exp(y))
print(math.log10(y))
print('-'*21)

z = 90
print(math.sin(z))
print(math.cos(z))
print(math.tan(z))
print('-'*21)

print('pi value ->',math.pi)
print('e value ->',math.e)
print('10 factorial = ',math.factorial(10))
print('-'*21)

#Random
import random
# a particular seed will generate similar value everytime
# random.seed(21)
print(random.random())
print(random.randint(1,11))
print(random.choice([1,2,53,21,45]))
print(random.sample([1,2,53,21,45],3)) # select random 3 from the list
print(random.uniform(1.0,3.0))
print('-'*21)

# DateTime
import datetime

print(datetime.datetime.now())
print(datetime.datetime(2017,12,21,10,30,0))

print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))

date1 = datetime.datetime(2017,12,21,10,30,0)
date2 = datetime.datetime.now()
print(date2 - date1)
print('-'*21)

#coLLECTIONS

from collections import Counter, defaultdict, OrderedDict

lst = [1,2,3,3,5,5,5]
print(Counter(lst))
print('-'*21)

d = defaultdict(int)
d['a'] += 2
print(d)
print('-'*21)

od = OrderedDict()
od['one'] = 1
od['zero'] = 0
print(od)
print('-'*21)

#strings
import string

print(string.ascii_letters)
print(string.ascii_uppercase)
print('-'*21)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print('-'*21)

print(string.punctuation)