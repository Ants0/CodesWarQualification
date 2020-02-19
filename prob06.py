sentence = input()
sentence = sentence[:len(sentence) - 1].split()
counter = 0
for word in sentence:
  if(word[0] == "N" or word[len(word) - 3:len(word)] == "N'T"):
    counter += 1
sentence = " ".join(sentence)
print(str(counter) + ": " + sentence)
