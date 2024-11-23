from lexer import tokenize

# Sample inputs for testing
inputs = [
    "let x = 10 + 5;",
    "let y = x * 2;",
    "print(x);",
    "print(y);",
    "let a = @;",  # Invalid character
]

for code in inputs:
    print(f"Input Code: {code}")
    try:
        tokens = tokenize(code)
        print("Tokens:", tokens)
    except SyntaxError as e:
        print(f"Error: {e}")
    print("=" * 50)
