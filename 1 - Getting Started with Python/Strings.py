#Strings

#Concatenation
print("P S"+'reyanshu')

#Replication
print('PSA'*11)
print('-'*25)

#Length
name = "P Sreyanshu Anupam"
print(f"{name} \n length = {len(name)}")
print('-'*25)

#Slicing
print(name[3:9])
print('negative index - ',name[-8:])
print('reverse index - ',name[:-9:-1])
print('reverse name - ',name[::-1])
print(name[:11])
print('-'*25)

#Case Conversion
print(name.upper())
print(name.lower())
print('-'*25)

#Strippin..
print("   Hey are you here ?         ".strip())
#lstrip and rstrip are also there
print('-'*25)

#Replace
print(name.replace('a','&'))
print(name.replace(' ','_'))
print('-'*25)

#Count
print(f"number of a or A's = {name.lower().count('a')}")
print('-'*25)

#find
print(name.find('reyansh'))
print('-'*25)

#String Check
print('Sreyanshu'.isalpha())
print("231".isdigit())
print('sreyanshu'.islower())
print("SREYANSHU".isupper())
print('-'*25)

#Captilization
print("p sreyanshu anupam".capitalize())
print("p sreyanshu anupam".title())
print('-'*25)

#starts_with and ends_with
print(name.startswith('P'))
print(name.endswith('am'))
print('-'*25)

#
print("Amulya Rattan".center(21,"*"))
print("Amulya Rattan".ljust(21,"*"))
print("Amulya Rattan".rjust(21,"*"))
print('-'*25)