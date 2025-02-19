import re

class SymbolTable:
    def __init__(self):
        self.table = {}

    def declare(self, var_name, var_type, value=None):
        """ Declare a variable in the symbol table. """
        if var_name in self.table:
            raise ValueError(f"Error: '{var_name}' already declared.")
        self.table[var_name] = {'type': var_type, 'value': value}

    def lookup(self, var_name):
        """ Look up a variable in the symbol table. """
        if var_name not in self.table:
            raise ValueError(f"Error: '{var_name}' used before declaration.")
        return self.table[var_name]

    def __repr__(self):
        """ Display the symbol table in a tabular format. """
        header = f"{'Variable':<10} {'Type':<10} {'Value':<10}"
        rows = [f"{key:<10} {value['type']:<10} {value['value']:<10}" for key, value in self.table.items()]
        return '\n'.join([header] + rows)


class ASTNode:
    def __init__(self, node_type, value=None, left=None, right=None, var_type=None):
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right
        self.var_type = var_type  # Type of the variable or expression

    def __repr__(self):
        return f"{self.node_type}({self.value}, Type: {self.var_type})"


def type_check(expr1, expr2, operator, line_number):
    """ Perform type checking for basic operations. """
    if operator == '+':
        if expr1['type'] == 'int' and expr2['type'] == 'int':
            return 'int'
        elif expr1['type'] == 'str' and expr2['type'] == 'str':
            return 'str'
        elif (expr1['type'] == 'int' and expr2['type'] == 'float') or (expr1['type'] == 'float' and expr2['type'] == 'int'):
            return 'float'
        else:
            raise ValueError(f"Error on line {line_number}: Type mismatch in '{expr1.value} {operator} {expr2.value}' ({expr1['type']} + {expr2['type']} not allowed)")

    elif operator == '-':
        if (expr1['type'] in ['int', 'float']) and (expr2['type'] in ['int', 'float']):
            return 'float' if 'float' in [expr1['type'], expr2['type']] else 'int'
        else:
            raise ValueError(f"Error on line {line_number}: Type mismatch in '{expr1.value} {operator} {expr2.value}' ({expr1['type']} - {expr2['type']} not allowed)")

    elif operator == '*':
        if (expr1['type'] in ['int', 'float']) and (expr2['type'] in ['int', 'float']):
            return 'float' if 'float' in [expr1['type'], expr2['type']] else 'int'
        elif expr1['type'] == 'str' and expr2['type'] == 'int':
            return 'str'
        elif expr1['type'] == 'int' and expr2['type'] == 'str':
            return 'str'
        else:
            raise ValueError(f"Error on line {line_number}: Type mismatch in '{expr1.value} {operator} {expr2.value}' ({expr1['type']} * {expr2['type']} not allowed)")

    elif operator == '/':
        if (expr1['type'] in ['int', 'float']) and (expr2['type'] in ['int', 'float']):
            return 'float'
        else:
            raise ValueError(f"Error on line {line_number}: Type mismatch in '{expr1.value} {operator} {expr2.value}' ({expr1['type']} / {expr2['type']} not allowed)")

    return None


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, statements):
        """ Analyze the statements and perform type checking and symbol table management. """
        line_number = 1
        for statement in statements:
            try:
                if isinstance(statement, AssignmentNode):
                    # Declare the variable
                    self.symbol_table.declare(statement.var_name, statement.var_type, statement.value)

                    # Type check the expression (if it's an expression node)
                    if isinstance(statement.value, ASTNode):
                        statement.var_type = self._check_expression_type(statement.value, line_number)

                elif isinstance(statement, PrintNode):
                    # Check if variable in print is declared
                    self.symbol_table.lookup(statement.var_name)
                    if isinstance(statement.var_name, ASTNode):
                        self._check_expression_type(statement.var_name, line_number)

            except ValueError as e:
                print(f"\nError Output: {e}")  # Clean error message output

            line_number += 1

    def generate_ast(self, statements):
        """ Generate the Abstract Syntax Tree (AST) for the given statements. """
        return [self._create_ast(statement) for statement in statements]

    def _create_ast(self, statement):
        """ Create an AST node based on the statement type (assignment, print, etc.). """
        if isinstance(statement, AssignmentNode):
            left = ASTNode('Variable', statement.var_name, var_type=statement.var_type)
            right = ASTNode('Literal', statement.value)
            return ASTNode('Assignment', statement.var_name, left, right, statement.var_type)
        elif isinstance(statement, PrintNode):
            var_node = ASTNode('Variable', statement.var_name)
            return ASTNode('Print', statement.var_name, var_type=self.symbol_table.lookup(statement.var_name)['type'])
        return None

    def _check_expression_type(self, expr_node, line_number):
        """ Check type of an expression (left and right operands). """
        left_type = self._get_expression_type(expr_node.left, line_number)
        right_type = self._get_expression_type(expr_node.right, line_number)
        return type_check(left_type, right_type, expr_node.value, line_number)

    def _get_expression_type(self, expr, line_number):
        """ Get type of the expression. """
        if isinstance(expr, ASTNode):
            return self.symbol_table.lookup(expr.value)
        else:
            return {'type': 'int'}  # Assuming integer type for literals for simplicity


class AssignmentNode:
    def __init__(self, var_name, var_type, value):
        self.var_name = var_name
        self.var_type = var_type
        self.value = value


class PrintNode:
    def __init__(self, var_name):
        self.var_name = var_name


def get_user_input():
    statements = []

    while True:
        print("\nEnter a statement:")
        print("1. Assignment (e.g., x = 5)")
        print("2. Print (e.g., print(x))")
        print("3. End input")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            var_name = input("Enter variable name: ")
            var_type = input("Enter variable type (int/float/str): ").strip()
            value = input("Enter value (literal or variable): ").strip()

            if var_type == "int":
                value = int(value)
            elif var_type == "float":
                value = float(value)
            elif var_type == "str":
                value = str(value)

            statement = AssignmentNode(var_name, var_type, value)
            statements.append(statement)
        elif choice == "2":
            var_name = input("Enter variable name to print: ")
            statement = PrintNode(var_name)
            statements.append(statement)
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please choose again.")

    return statements


# Main execution
if __name__ == "__main__":
    print("Welcome to the semantic analyzer.")
    statements = get_user_input()

    analyzer = SemanticAnalyzer()
    analyzer.analyze(statements)

    print("\nSymbol Table:")
    print(analyzer.symbol_table)

    print("\nAST:")
    ast = analyzer.generate_ast(statements)
    for node in ast:
        print(node)
