import unittest
from io import StringIO
import sys
from lexer import tokenize
from parser import Parser
from interpreter import Interpreter
from ast_nodes import AssignNode, PrintNode, BinOpNode, VarNode


class TestInterpreter(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # Reset stdout after each test
        sys.stdout = sys.__stdout__

    # Milestone 1: Lexical Analysis
    def test_lexer_valid_input(self):
        code = "let x = 10 + 5; print(x);"
        expected_tokens = [
            ('LET', 'let', 1, 1), ('ID', 'x', 1, 5), ('ASSIGN', '=', 1, 7),
            ('NUMBER', '10', 1, 9), ('PLUS', '+', 1, 12), ('NUMBER', '5', 1, 14),
            ('SEMI', ';', 1, 15), ('PRINT', 'print', 1, 17), ('LPAREN', '(', 1, 22),
            ('ID', 'x', 1, 23), ('RPAREN', ')', 1, 24), ('SEMI', ';', 1, 25)
        ]
        tokens = tokenize(code)
        self.assertEqual(tokens, expected_tokens)

    def test_lexer_invalid_input(self):
        code = "let x = @;"
        with self.assertRaises(SyntaxError):
            tokenize(code)

    # Milestone 2: Parsing
    def test_parser_valid_ast(self):
        code = "let x = 10 + 5; print(x);"
        tokens = tokenize(code)
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(len(ast), 2)  # Two nodes: AssignNode and PrintNode
        self.assertIsInstance(ast[0], AssignNode)
        self.assertIsInstance(ast[1], PrintNode)

    def test_parser_invalid_syntax(self):
        code = "let x = ;"
        tokens = tokenize(code)
        parser = Parser(tokens)
        with self.assertRaises(SyntaxError):
            parser.parse()

    # Milestone 3: Interpretation
    def test_interpreter_execution(self):
        code = "let x = 10 + 5; let y = x * 2; print(x); print(y);"
        tokens = tokenize(code)
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        interpreter.interpret(ast)
        output = self.captured_output.getvalue().strip()
        self.assertEqual(output, "15\n30")

    def test_interpreter_undefined_variable(self):
        code = "print(z);"
        tokens = tokenize(code)
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        with self.assertRaises(RuntimeError):
            interpreter.interpret(ast)

    def test_interpreter_zero_division(self):
        code = "let x = 10 / 0; print(x);"
        tokens = tokenize(code)
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        with self.assertRaises(ZeroDivisionError):
            interpreter.interpret(ast)

if __name__ == "__main__":
    unittest.main()
