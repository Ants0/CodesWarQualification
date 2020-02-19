import math
jar = int(input())
num = int(input())
closest = math.inf
name = ""
for i in range(num):
  person = input()
  person = person.split()
  if(jar > int(person[0])):
    if(jar - int(person[0]) < closest):
      closest = jar - int(person[0])
      name = person[1]
    elif(jar - int(person[0]) == closest):
      name += " " + person[1]
  elif(jar < int(person[0])):
    if(int(person[0]) - jar < closest):
      closest = int(person[0]) - jar
      name = person[1]
    elif(int(person[0]) - jar == closest): 
      name += " " + person[1]
print(name)
