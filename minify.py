import sys
import os

filename = open(sys.argv[1], "r")
new = open("output.tacapl", "w")
contents = filename.read()

newThing = contents.strip()

i = 0

listThing = []

for char in newThing:
    listThing.append(char)

quoteCount = 0

print(listThing)

while i < len(listThing):
    if listThing[i] == "\"":
        quoteCount+=1
    if listThing[i] == "\n" and quoteCount % 2 == 0:
        listThing.pop(i)
        i-=1
    i += 1

stringThing = ""
print(listThing)
for thing in listThing:
    stringThing += str(thing)

new.write(stringThing)

print("Done!")
