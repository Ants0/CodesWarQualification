x = int(input()) 
for i in range(x):
  num = input()
  try:
      letters = ""
      num = int(num)
      if(num >= 50000):
        letters += "PM"
        num -= 50000
      if(num >= 10000):
        letters += "M" * int(num / 10000)
        num -= (10000 * int(num / 10000))
      if (num >= 5000):
        letters += "PC"
        num -= 5000
      if (num >= 1000):
        letters += "C" * int(num / 1000)
        num -= (1000 * int(num / 1000))
      if (num >= 500):
        letters += "PH"
        num -= 500
      if (num >= 100):
        letters += "H" * int(num / 100)
        num -= (100 * int(num / 100))
      if (num >= 50):
        letters += "PD"
        num -= 50
      if (num >= 10):
        letters += "D" * int(num / 10)
        num -= (10 * int(num / 10))
      if(num >= 6):
        letters += "PI"
        num -= 6
      if (num >= 1):
          letters += "I" * int(num / 1)
          num -= (1 * int(num / 1))
      print(letters)
      print(num)
  except ValueError:
      counter = 0
      x = "IPDHCM"
      placeholder = ""
      for char in num:
          placeholder += char + " "
      num = placeholder.split()
      for i in range(len(num)):
          if(num[i] == "I"):
              counter += 1
          if (num[i] == "P"):
              if (num[i + 1] == "I"):
                  counter += 5 * 1
              if (num[i + 1] == "D"):
                  counter += 4 * 10
              if (num[i + 1] == "H"):
                  counter += 4 * 100
              if (num[i + 1] == "C"):
                  counter += 4 * 1000
              if (num[i + 1] == "M"):
                  counter += 4 * 10000
          if (num[i] == "D"):
              counter += 10
          if (num[i] == "H"):
              counter += 100
          if (num[i] == "C"):
              counter += 1000
          if (num[i] == "M"):
              counter += 10000
      print(counter)
