import sys
import os

filename = open(sys.argv[1], "r")
new = open("output.tacapl", "w")
contents = filename.read()

newThing = contents.strip()

newThingAgain = ""

for item in newThing:
    if item != "\n":
        newThingAgain+=item

new.write(newThingAgain)

print("Done!")
