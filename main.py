f = open("zen_text.txt")
Count = 0
Content = f.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Count += 1

print("This is the number of lines in the file :")
print(Count)
