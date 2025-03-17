import Agent

a1 = Agent.agent("mario",18)
print(dir(a1))
a1.info()

print('-'*21)

a1 = Agent.agent("Shaktimaan",40)
a1.health *= 100
a1.info()
print('-'*21)
a2 = Agent.agent("Gangadhar",40)
a2.health *= 100
a2.info()
print('-'*21)
a3 = Agent.boss("Michael Scott",99)
a3.health *= 100
a3.info()
print('-'*21)