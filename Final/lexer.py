import re
##The lexer will break down the input code into tokens
# Define token types
LET = 'LET'
ID = 'ID'
ASSIGN = 'ASSIGN'
NUMBER = 'NUMBER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
SEMI = 'SEMI'
PRINT = 'PRINT'
LPAREN = 'LPAREN'  # Left parenthesis
RPAREN = 'RPAREN'  # Right parenthesis

# Token specifications using regular expressions
token_specification = [
    (LET, r'\blet\b'),            # 'let' keyword
    (PRINT, r'\bprint\b'),        # 'print' keyword
    (ID, r'[a-zA-Z_][a-zA-Z_0-9]*'),  # Identifiers
    (ASSIGN, r'='),               # Assignment operator
    (NUMBER, r'\d+'),             # Integer numbers
    (PLUS, r'\+'),                # Plus operator
    (MINUS, r'-'),                # Minus operator
    (MUL, r'\*'),                 # Multiplication operator
    (DIV, r'/'),                  # Division operator
    (SEMI, r';'),                 # Semicolon
    (LPAREN, r'\('),              # Left parenthesis
    (RPAREN, r'\)'),              # Right parenthesis
    (r'WHITESPACE', r'\s+'),      # Whitespace (ignored)
]

# Tokenizer function
def tokenize(code):
    tokens = []
    position = 0
    line = 1
    column = 1
    while position < len(code):
        match = None
        for token_type, pattern in token_specification:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                if token_type != 'WHITESPACE':  # Skip whitespace
                    tokens.append((token_type, match.group(), line, column))
                position = match.end()
                column += len(match.group())
                break
        if not match:
            raise SyntaxError(f"Unexpected character '{code[position]}' at line {line}, column {column}")
        if code[position - 1] == '\n':  # If newline, increment line and reset column
            line += 1
            column = 1

    return tokens

# Test the lexer
if __name__ == "__main__":
    code = "let x = 10 + 5; print(x);"
    tokens = tokenize(code)
    print(tokens)


