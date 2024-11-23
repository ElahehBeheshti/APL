from ast_nodes import *
from ast_nodes import AssignNode, PrintNode, BinOpNode, VarNode


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current_token(self):
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def consume(self, expected_type):
        token = self.current_token()
        if token and token[0] == expected_type:
            self.position += 1
            return token
        else:
            line, column = token[2], token[3] if token else (None, None)
            raise SyntaxError(f"Expected {expected_type}, found {token} at line {line}, column {column}")

    def parse(self):
        nodes = []
        while self.current_token():
            nodes.append(self.parse_statement())
        return nodes

    def parse_statement(self):
        token = self.current_token()
        if token[0] == 'LET':
            return self.parse_assignment()
        elif token[0] == 'PRINT':
            return self.parse_print()
        else:
            line, column = token[2], token[3]
            raise SyntaxError(f"Unexpected token '{token[1]}' at line {line}, column {column}")

    def parse_assignment(self):
        let_token = self.consume('LET')
        var_name = self.consume('ID')[1]
        self.consume('ASSIGN')
        expr = self.parse_expression()
        if expr is None:
            raise SyntaxError(f"Missing value after '=' in assignment to '{var_name}' at line {let_token[2]}, column {let_token[3]}")
        if not self.current_token() or self.current_token()[0] != 'SEMI':
            line, column = self.current_token()[2], self.current_token()[3]
            raise SyntaxError(f"Missing semicolon at the end of assignment to '{var_name}' at line {line}, column {column}")
        self.consume('SEMI')
        return AssignNode(var_name, expr, let_token[2], let_token[3])

    def parse_print(self):
        print_token = self.consume('PRINT')
        self.consume('LPAREN')
        expr = self.parse_expression()
        if self.current_token() and self.current_token()[0] == 'SEMI':
            raise SyntaxError(f"Misplaced ';' in print statement at line {self.current_token()[2]}, column {self.current_token()[3]}. Missing closing ')'.")
        if not self.current_token() or self.current_token()[0] != 'RPAREN':
            raise SyntaxError(f"Unmatched '(' in print statement, missing ')' at line {print_token[2]}, column {print_token[3]}")
        self.consume('RPAREN')
        if not self.current_token() or self.current_token()[0] != 'SEMI':
            line, column = self.current_token()[2], self.current_token()[3]
            raise SyntaxError(f"Missing semicolon at the end of print statement at line {line}, column {column}")
        self.consume('SEMI')
        return PrintNode(expr)

    def parse_expression(self):
        left = self.parse_term()
        while self.current_token() and self.current_token()[0] in ('PLUS', 'MINUS'):
            op_token = self.consume(self.current_token()[0])
            op = op_token[1]
            right = self.parse_term()
            if right is None:
                raise SyntaxError(f"Missing operand after '{op}' at line {op_token[2]}, column {op_token[3]}")
            left = BinOpNode(left, op, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.current_token() and self.current_token()[0] in ('MUL', 'DIV'):
            op_token = self.consume(self.current_token()[0])
            op = op_token[1]
            right = self.parse_factor()
            if right is None:
                raise SyntaxError(f"Missing or invalid operand after '{op}' at line {op_token[2]}, column {op_token[3]}")
            left = BinOpNode(left, op, right)
        return left

    def parse_factor(self):
        token = self.current_token()
        if token[0] == 'NUMBER':
            self.consume('NUMBER')
            return int(token[1])
        elif token[0] == 'ID':
            self.consume('ID')
            return VarNode(token[1])
        elif token[0] == 'LPAREN':
            lparen_token = self.consume('LPAREN')
            expr = self.parse_expression()
            if not self.current_token() or self.current_token()[0] != 'RPAREN':
                line, column = lparen_token[2], lparen_token[3]
                raise SyntaxError(f"Unmatched '(' at line {line}, column {column}")
            self.consume('RPAREN')
            return expr
        else:
            line, column = token[2], token[3] if token else (None, None)
            raise SyntaxError(f"Invalid expression at line {line}, column {column}")
