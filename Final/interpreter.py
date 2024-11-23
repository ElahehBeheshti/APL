from ast_nodes import *
from ast_nodes import AssignNode, PrintNode, BinOpNode, VarNode


class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, nodes):
        for node in nodes:
            self.execute(node)

    def execute(self, node):
        if isinstance(node, AssignNode):
            self.variables[node.var_name] = self.evaluate(node.expr)
        elif isinstance(node, PrintNode):
            print(self.evaluate(node.expr))
        else:
            raise RuntimeError(f"Unknown node type: {node}")

    def evaluate(self, expr):
        if isinstance(expr, int):
            return expr
        elif isinstance(expr, VarNode):
            if expr.name in self.variables:
                return self.variables[expr.name]
            raise RuntimeError(f"Undefined variable: {expr.name}")
        elif isinstance(expr, BinOpNode):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)
            if expr.op == '+':
                return left + right
            elif expr.op == '-':
                return left - right
            elif expr.op == '*':
                return left * right
            elif expr.op == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                return left / right

