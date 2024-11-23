from lexer import tokenize
from parser import Parser

# Sample inputs for testing
inputs = [
    "let x = 10 + 5;",
    "print(x);",
    "let y = x * 2;",
    "let z = 10 + ;",  # Invalid expression
]

for code in inputs:
    print(f"Input Code: {code}")
    try:
        tokens = tokenize(code)
        print("Tokens:", tokens)
        parser = Parser(tokens)
        ast = parser.parse()
        print("AST:", ast)
    except SyntaxError as e:
        print(f"Error: {e}")
    print("=" * 50)
