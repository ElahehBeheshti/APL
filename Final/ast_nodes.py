# AST Node for variable assignment
class AssignNode:
    def __init__(self, var_name, expr,line, column):
        self.var_name = var_name
        self.expr = expr
        self.line = line
        self.column = column

# AST Node for binary operations (like +, -, *, /)
class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

# AST Node for variable references
class VarNode:
    def __init__(self, name):
        self.name = name

# AST Node for printing values
class PrintNode:
    def __init__(self, expr):
        self.expr = expr
