from tacapl import Interpreter
import sys

filename = open(sys.argv[1], "r")
contents = filename.read()

TACAPL = Interpreter()
TACAPL.run(str(contents))