import math
t = float(input())
p = round(100 * math.sqrt(t) + 201/(t+1)+1)
print(str(int(t)) + " " + str(p))
