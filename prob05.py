sentence = input()
list1 = []
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pangram = -1
counter = 0
boolean = True
for letter in sentence:
  if(letter == " "):
    continue
  else:
    list1 += letter
list2 = list1[1:len(list1)]
for char in alpha:
  if(char in list1):
    counter += 1
if(counter == 26):
  pangram = 0
  for char in list1:
    for letter in list2:
      if(char == letter):
        print(char, letter)
        boolean = False
      list2 = list2[1:]
if(boolean == True and counter == 26):
  pangram = 1
if(pangram == -1):
  print("Neither: " + sentence)
if(pangram == 0):
  print("Pangram: " + sentence)
if(pangram == 1):
  print("Perfect: " + sentence)
