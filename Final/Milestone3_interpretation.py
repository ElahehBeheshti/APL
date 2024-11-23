from lexer import tokenize
from parser import Parser
from interpreter import Interpreter

# Sample inputs for testing
inputs = [
    "let x = 10 + 5; print(x);",
    "let y = x * 2; print(y);",
    "let z = 10 / 0;",  # Division by zero
    "print(unknown);",  # Undefined variable
]

for code in inputs:
    print(f"Input Code: {code}")
    try:
        tokens = tokenize(code)
        print("Tokens:", tokens)
        parser = Parser(tokens)
        ast = parser.parse()
        print("AST:", ast)
        interpreter = Interpreter()
        interpreter.interpret(ast)
    except Exception as e:
        print(f"Error: {e}")
    print("=" * 50)
