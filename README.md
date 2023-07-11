# TACAPL
## Why to Use:
- ~~I made it~~
- An actually simple syntax this time
- Errors are understandable
## How to Use:
### Running:
If you have the entire project downloaded, you can run `python main.py <yourfile>.tacapl` in your terminal.

If you only have the library installed, this would be your code:

    from  tacapl  import  Interpreter
    
    TACAPL  =  Interpreter()
    TACAPL.run(str(contents))

### Commands:
`print <whatto print>` - Self explanatory

`set <variable> = <value>` - Sets a variable

`add <num1> + <num2>` - Self explanatory

`subtract <num1> - <num2>` - Self explanatory

`multiply <num1> * <num2>` - Self explanatory

`divide <num1> / <num2>` - Self explanatory

`if <condition>` - This will be explained later

`end` - This will be explained later

`input <variable> = "<question>"` - Sets the variable to the user's input

`printsent <whattoprint>` - Same as `print` but without a new line

### Explained Later:
`if <condition>` and `end`: These commands go hand in hand, if the condition is true, nothing happens, but if the condition is false, no code will run until the statement that says `end`.

### Conventions:
Every line but the last line must end in a semicolon.


