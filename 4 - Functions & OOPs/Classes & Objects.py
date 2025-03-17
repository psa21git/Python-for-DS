class person:
    name = "PSA"
    age = 20

p1 = person()
print(p1.name)
print('-'*21)

p2 = person()
p2.name = "Millie"
print(p2.name)
print('-'*21)

class mathematics:
    name = "PK"

    def greet(self):
        print("Gd M0rning",self.name)

    def lst_dot(self,lst_1,lst_2):
        return [lst_1[i]*lst_2[i] for i in range(len(lst_1))]


m = mathematics()
m.greet()
print(m.lst_dot([1,2,3],[4,5,6]))