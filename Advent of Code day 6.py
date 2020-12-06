
f = open("input.txt")
inputList = f.read().splitlines()
f.close()

answers = []
count = 0
total = 0

for x in inputList:
    if x != "":
        for i in range(len(x)):
            if x[i] not in answers:
                
                answers.append(x[i])
                count = count + 1
    else:
        answers.clear()
        total = total + count
        count = 0
print(total)