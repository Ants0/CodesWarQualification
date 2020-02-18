num = input()
try:
    letters = ""
    num = int(num)
    if(num > 10000):
        if(num > 50000):
            letters += "PM"
            num -= 50000
        else:
            letters += "M" * (num / 10000)
            num - (10000 *(num / 10000))
    if (num > 1000):
        if (num > 5000):
            letters += "PC"
            num -= 5000
        else:
            letters += "C" * (num / 1000)
            num - (1000 * (num / 1000))
    if (num > 100):
        if (num > 500):
            letters += "PH"
            num -= 500
        else:
            letters += "H" * (num / 100)
            num - (100 * (num / 100))
    if (num > 10):
        if (num > 50):
            letters += "PD"
            num -= 50
        else:
            letters += "D" * (num / 10)
            num - (10 * (num / 10))
    if (num > 5):
        if(num > 6):

    if (num > 1):
        letters += "I" * (num / 1)
        num - (1 * (num / 1))
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
