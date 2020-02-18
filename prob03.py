num = int(input("Enter the number of time values: "))
final = 0
for i in range(num):
  timeValue = input("Enter a time value: ")
  length = len(timeValue)
  final = 20
  for char in timeValue:
      if(char == ":"):
          continue
      if(char == "1"):
        final += 2 * 15
      if(char == "7"):
        final += 3 * 15
      if(char == "4"):
        final += 4 * 15
      if(char == "2" or char == "3" or char == "5"):
        final += 5 * 15
      if(char == "6" or char == "9" or char == "0"):
        final += 6 * 15
      if(char == "8"):
        final += 7 * 15
  print(final)
