import sys
import json
class SemanticAnalyzer:
    def __init__(self, syntax_tree, symbol_table):
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
        # Assuming your list is named `my_list` and `identifier` is the value you're looking for
        for sublist in self.symbol_table:
            if sublist[0] == identifier:
                match_found = True
                break
            if not match_found:
                raise NameError(f"Undeclared identifier: {identifier}")



if __name__=='__main__':
    with open('syn_tree.json', "r") as file:
        syntax_tree = json.load(file)
        
    with open('table.json', "r") as file:
        symbol_table = json.load(file)


    # Perform semantic analysis
    semantic_analyzer = SemanticAnalyzer(syntax_tree, symbol_table)
    semantic_analyzer.analyze()
