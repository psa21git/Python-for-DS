try:
    x = 10
    print(int("ashjdg"))
    print(x/0)
except ZeroDivisionError:
    print("Divisor is Zero!")
except:
    print("Unknown Error Ho gaya!")
else:
    print("Try with no Errors")
finally:
    print("Always executed!")
print("-"*30)

try:
    num1,num2 = 10,5
    print(num1/num2)
except ZeroDivisionError as zde:
    print(zde)
except Exception as e:
    print(e)
else:
    print("Everything is fine!")
finally:
    print("Program End!")