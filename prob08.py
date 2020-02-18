sentence = input()
sentence = sentence.split()
print(sentence[(len(sentence) - 1) - int(sentence[0])])
