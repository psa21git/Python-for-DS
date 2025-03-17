class person:

    # def __init__(self):
    #     print("hello")

    def __init__(self,name="asish",age=19):
        print(name,age)
        self.name = name
        self.age = age

    def run(self):
        print(self.name)
        print("run!")

# p1 = person()
# p2 = person("PSA",21)
# p2.run()
# p1.run()
print('-'*21)

class agent:

    def __init__(self,name,age):
        print("Welcome to the GAME!")
        self.name  = name
        self.age = age
        self.health = 100
        self.alive  = True

    def curr_health(self):
        print(f"Current health of {self.name} is {self.health}")

    def punched(self):
        self.health -= 10

    def shooted(self):
        self.health -= 50

    def is_alive(self):
        if self.health<=0:
            self.alive = False
    # if alive == False:

    def info(self):
        self.is_alive()
        print("Name   : ",self.name)
        print("Age    : ",self.age)
        print("Health : ",self.health)
        print("Alive  : ",self.alive)

a1 = agent("Aishwarya",23)
a1.curr_health()
a1.punched()
a1.shooted()
a1.info()
print('-'*21)

a2 = agent("Mandy",29)
a2.curr_health()
a2.shooted()
a2.shooted()
a2.info()
print('-'*21)

class boss(agent):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.health = 1000
        self.alive  = True

    def blow_fire(self):
        print("blow_fire!")

bs = boss("Akshaya",999)
bs.blow_fire()
bs.info()
