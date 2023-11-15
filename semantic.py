import sys
import json
class SemanticAnalyzer:
    def __init__(self, syntax_tree):
        self.syntax_tree = syntax_tree
        self.symbol_table = {}  # You can use this to store variable names and types, if necessary

    def analyze(self):
        self.visit(self.syntax_tree)

    def visit(self, node):
        if isinstance(node, list):
            for child in node:
                self.visit(child)
        elif isinstance(node, str):
            # Handle identifiers, strings, reserved words, etc.
            self.visit_identifier(node)
        elif isinstance(node, float) or isinstance(node, int):
            # Handle numbers
            pass
        else:
            raise Exception(f"Unrecognized node type: {type(node)}")

    def visit_identifier(self, identifier):
        # Implement rules for identifiers
        # Example: Check if the identifier is declared in the symbol table
        if identifier not in self.symbol_table:
            raise NameError(f"Undeclared identifier: {identifier}")

# ... rest of your existing code ...

if __name__=='__main__':
    with open('table.json', "r") as file:
        lines = json.load(file)

    parser = Parser(lines)
    syntax_tree = parser.parse()
    print(syntax_tree)
    tree_print(syntax_tree)

    # Perform semantic analysis
    semantic_analyzer = SemanticAnalyzer(syntax_tree)
    semantic_analyzer.analyze()
