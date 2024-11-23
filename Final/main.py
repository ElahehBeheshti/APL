from lexer import tokenize
from parser import Parser
from interpreter import Interpreter

def show_error_context(code, line, column):
    lines = code.splitlines()
    error_line = lines[line - 1]
    pointer = ' ' * (column - 1) + '^'
    return f"{error_line}\n{pointer}"

def run_test_case(code):
    print(f"\nTesting Code: {code}")
    try:
        tokens = tokenize(code)
        print(f"Tokens: {tokens}")
        parser = Parser(tokens)
        ast = parser.parse()
        print(f"AST: {ast}")
        interpreter = Interpreter()
        interpreter.interpret(ast)
        print("Execution successful!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        if hasattr(e, 'line') and hasattr(e, 'column'):
            print(show_error_context(code, e.line, e.column))
        return False

if __name__ == "__main__":
    test_cases = [
        "let x = 10 + 5; print(x);",
        "let x = ;",
        "print(10 + 5;",
        "let x = 10 print(x);",
        "let x = @;",
        "let x = 10 + ;",
        "let y = 10; print(y;)",
    ]

    passed = 0
    total = len(test_cases)

    for code in test_cases:
        print("=" * 50)
        if run_test_case(code):
            passed += 1
        print("=" * 50)

    print(f"\nSummary: {passed}/{total} test cases passed.")
