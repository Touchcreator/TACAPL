skip_code = False
commands = ["print", "set", "add", "subtract", "multiply", "divide", "if", "end", "input", "printsent", "ifstr"]
op_one = ""
op_two = ""

class Interpreter:
    def __init__(self):
        self.variables = {}

    def run(self, code):
        global statenum
        statenum = 1
        statements = code.split(";")
        for statement in statements:
            self.execute(statement.strip())
            statenum += 1

    def execute(self, statement):
        global skip_code
        global commands
        global op_one, op_two
        tokens = statement.split(" ")
        command = tokens[0]
        if skip_code == True and command != "end":
            command = ""

        commands = ["print", "set", "add", "subtract", "multiply", "divide", "if", "end", "input", "printsent", "ifstr"]

        if command == "print":
            value = " ".join(tokens[1:])  # Combine all tokens after 'print' as the value
            if value.startswith('"') and value.endswith('"'):
                # Print a string literal
                print(value[1:-1])
            elif value in self.variables:
                # Print a variable value
                print(self.variables[value])
        if command == "printsent":
            value = " ".join(tokens[1:])  # Combine all tokens after 'print' as the value
            if value.startswith('"') and value.endswith('"'):
                # Print a string literal
                print(value[1:-1], end="")
            elif value in self.variables:
                # Print a variable value
                print(self.variables[value], end="")
        elif command == "set":
            variable = tokens[1]
            value = " ".join(tokens[3:])  # Combine all tokens after 'set variable =' as the value
            self.variables[variable] = value
        elif command == "add":
            variable = tokens[1]
            opop_one = tokens[3]  # in case there's an error
            opop_two = tokens[5]
            try:
                op_one = float(tokens[3])
            except ValueError:
                op_one = float(self.variables[opop_one])
            try:
                op_two = float(tokens[5])
            except ValueError:
                op_two = float(self.variables[opop_two])
            self.variables[variable] = op_one + op_two
        elif command == "subtract":
            variable = tokens[1]
            opop_one = tokens[3]  # in case there's an error
            opop_two = tokens[5]
            try:
                op_one = float(tokens[3])
            except ValueError:
                op_one = float(self.variables[opop_one])
            try:
                op_two = float(tokens[5])
            except ValueError:
                op_two = float(self.variables[opop_two])
            self.variables[variable] = op_one - op_two
        elif command == "multiply":
            variable = tokens[1]
            opop_one = tokens[3]  # in case there's an error
            opop_two = tokens[5]
            try:
                op_one = float(tokens[3])
            except ValueError:
                op_one = float(self.variables[opop_one])
            try:
                op_two = float(tokens[5])
            except ValueError:
                op_two = float(self.variables[opop_two])
            self.variables[variable] = op_one * op_two
        elif command == "divide":
            variable = tokens[1]
            opop_one = tokens[3]  # in case there's an error
            opop_two = tokens[5]
            try:
                op_one = float(tokens[3])
            except ValueError:
                op_one = float(self.variables[opop_one])
            try:
                op_two = float(tokens[5])
            except ValueError:
                op_two = float(self.variables[opop_two])
            if op_two != 0:
                self.variables[variable] = op_one / op_two
            else:
                print("Error: Division by zero!")
        # Add more commands as needed
        elif command == "if":
            condition = tokens[1:]
            operation = condition[1]
            opop_one = condition[0]  # in case there's an error
            opop_two = condition[2]
            try:
                op_one = float(condition[0])
            except ValueError:
                op_one = float(self.variables[opop_one])
            try:
                op_two = float(condition[2])
            except ValueError:
                op_two = float(self.variables[opop_two])

            # check for the answer
            if operation == ">":
                skip_code = not op_one > op_two
            if operation == "<":
                skip_code = not op_one < op_two
            if operation == ">=":
                skip_code = not op_one >= op_two
            if operation == "<":
                skip_code = not op_one <= op_two
            if operation == "==":
                skip_code = not op_one == op_two
            if operation == "!=":
                skip_code = not op_one != op_two
        elif command == "ifstr":
            condition = tokens[1:]
            operation = condition[1]
            opop_one = condition[0]  # in case there's an error
            opop_two = condition[2]
            if opop_one.startswith('"') and opop_one.endswith('"'):
                # Print a string literal
                op_one = opop_one
            elif opop_one in self.variables:
                op_one = self.variables[opop_one]
            if opop_two.startswith('"') and opop_two.endswith('"'):
                # Print a string literal
                op_two = opop_two
            elif opop_two in self.variables:
                op_two = self.variables[opop_two]
            # check for the answer
            if operation == "==":
                skip_code = not str(op_one) == str(op_two)
                print(skip_code)
            if operation == "!=":
                skip_code = not str(op_one) != str(op_two)
        elif command == "end":
            skip_code = False
        elif command == "input":
            variable = tokens[1]
            value = " ".join(tokens[3:])  # Combine all tokens after 'set variable =' as the value
            self.variables[variable] = input(value[1:-1])
        elif tokens[0] not in commands:
            print("Error at \"" + statement + "\" Statement " + str(statenum) + ". Maybe it's a typo or a missing semicolon?")
            exit()
