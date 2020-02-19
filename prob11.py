while True:
  num = input()
  num = num.split()
  a = int(num[0])
  b = int(num[1])
  c = int(num[2])
  x = int(num[3])
  y = int(num[4])
  z = int(num[5])
  if(a != -1 and b != -1 and c != -1 and x != -1 and y != -1 and z != -1):
    n = 0
    while True: 
      if(n % a == x and n % b == y and n % c == z):
        break
      else:
        n += 1
    print(n)
  else:
    break
