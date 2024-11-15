skip_code = False
commands = ["print", "set", "add", "subtract", "multiply", "divide", "if", "end", "input", "printsent", "ifstr"]
equalsCommands = ["set", "add", "subtract", "multiply", "divide", "input"]
op_two = ""


class Interpreter:
    def error(self, statement):
        print("\n\nError at \"" + str(statement) + "\" , Statement " + str(statenum) + ". Maybe it's a typo or a missing semicolon?\n")
        exit()
    
    def equalError(self, statement):
        print("\n\nError at \"" + str(statement) + "\" , Statement " + str(statenum) + ". You need an equals sign when you're changing or setting variables.\n")
        exit()

    def ifError(self, statement):
        print("\n\nError at \"" + str(statement) + "\" , Statement " + str(statenum) + ". Your operation is not a possible operation choice\n")
        exit()

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
        if skip_code and command != "end":
            command = ""

        commands = ["print", "set", "add", "subtract", "multiply", "divide", "if", "end", "input", "printsent", "ifstr"]
        if command in equalsCommands:
            if tokens[2] != "=":
                self.equalError(statement)
        if command == "print":
            value = " ".join(tokens[1:])  # Combine all tokens after 'print' as the value
            if value.startswith('"') and value.endswith('"'):
                # Print a string literal
                print(value[1:-1])
            elif value in self.variables:
                # Print a variable value
                print(self.variables[value])
        elif command == "printsent":
            value = " ".join(tokens[1:])  # Combine all tokens after 'printsent' as the value
            if value.startswith('"') and value.endswith('"'):
                # Print a string literal
                print(value[1:-1], end="")
            elif value in self.variables:
                # Print a variable value
                print(self.variables[value], end="")
        elif command == "set":
            variable = tokens[1]
            value = " ".join(tokens[3:])  # Combine all tokens after 'set variable =' as the value
            value = value[1:-1]
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
        elif command == "if":
            condition = tokens[1:]
            operation = condition[1]
            opop_one = condition[0]  # in case there's an error
            opop_two = condition[2]
            op_one = opop_one  # Default to using variable name as the first operand
            op_two = opop_two  # Default to using variable name as the second operand

            # Check if the first operand is a variable and exists
            if opop_one in self.variables:
                op_one = self.variables[opop_one]

            # Check if the second operand is a variable and exists
            if opop_two in self.variables:
                op_two = self.variables[opop_two]

            # Check the condition based on the operation
            if operation == ">":
                skip_code = not (op_one > op_two)
            elif operation == "<":
                skip_code = not (op_one < op_two)
            elif operation == ">=":
                skip_code = not (op_one >= op_two)
            elif operation == "<=":
                skip_code = not (op_one <= op_two)
            elif operation == "==":
                skip_code = not (op_one == op_two)
            elif operation == "!=":
                skip_code = not (op_one != op_two)
            else:
                self.ifError(statement)
        elif command == "end":
            skip_code = False
        elif command == "input":
            variable = tokens[1]
            value = " ".join(tokens[3:])  # Combine all tokens after 'set variable =' as the value
            self.variables[variable] = input(value[1:-1])
        elif tokens[0] not in commands:
            self.error(statement)
