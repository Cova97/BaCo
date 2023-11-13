import sys
import json
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.next_token()
    
    def next_token(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = ('EOF', 'EOF')
    
    def parse(self):
        if self.current_token[0] == 'EOF':
            return None
        else:
            return self.parse_expr()
    
    def parse_expr(self):
        if self.current_token[0] == 'IPAREN':
            return self.parse_list()
        elif self.current_token[0] == 'NUMERO':
            return self.parse_number()
        elif self.current_token[0] == 'IDENTIFIER':
            return self.parse_identifier()
        elif self.current_token[0] == 'STRING':
            return self.parse_string()
        elif self.current_token[0] == 'RESERVED':
            return self.parse_reserved()
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token[1]}")
    
    def parse_reserved(self):
        op = self.current_token[1]
        self.next_token()  # consume 'IDENTIFICADOR'
        return op
    
    def parse_list(self):
        elements = []
        self.next_token()  # consume 'IPAREN'
        while self.current_token[0] != 'DPAREN':
            elements.append(self.parse_expr())
        self.next_token()  # consume 'DPAREN'
        return elements
    
    def parse_number(self):
        value = self.current_token[1]
        self.next_token()  # consume 'NUMERO'
        return float(value) #if '.' in value else int(value)
    
    def parse_identifier(self):
        name = self.current_token[1]
        self.next_token()  # consume 'IDENTIFICADOR'
        return name
    
    def parse_string(self):
        string_value = self.current_token[1]
        self.next_token()  # consume 'CADENA'
        return string_value
    
def tree_print(node, level=0):
    indent = '  ' * level
    if isinstance(node, list):
        print(indent + '[')
        for child in node:
            tree_print(child, level + 1)
        print(indent + ']')
    else:
        print(indent + str(node))
        
    
if __name__=='__main__':
    #name = sys.argv[1:]
    tokens =[]
    errors =[]
    with open ('table.json',"r") as file:
        lines = json.load(file)
        
    #print(lines)
    parser = Parser(lines)

    # Parse the tokens to build a syntax tree
    syntax_tree = parser.parse()
    print(syntax_tree)
    tree_print(syntax_tree)
        