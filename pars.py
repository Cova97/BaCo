import sys
import json
import pickle
class Node:
    def __init__(self, type, value=None, children=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        return f"{self.type}: {self.value} -> {self.children}"


def parse(tokens):
    def parse_expression(index):
        token_type, token_value = tokens[index]
        if token_type == 'IPAREN':
            return parse_list(index)
        elif token_type in ['NUMERO', 'IDENTIFIER', 'STRING', 'RESERVED']:
            return Node(token_type, token_value), index + 1
        else:
            raise ValueError(f"Unexpected token: {token_type}")

    def parse_list(index):
        children = []
        index += 1  # Skip the opening parenthesis
        while tokens[index][0] != 'DPAREN':
            node, index = parse_expression(index)
            children.append(node)
        return Node('LIST', children=children), index + 1

    ast, _ = parse_expression(0)
    return ast


    
if __name__=='__main__':
    #name = sys.argv[1:]
    tokens =[]
    errors =[]
    with open ('table.json',"r") as file:
        lines = json.load(file)
        
    #print(lines)
    # Parse the tokens
    ast = parse(lines)
    print(ast)
    

    # Parse the tokens to build a syntax tree
    # syntax_tree = parser.parse()
    with open ('syn_tree.pickle',"wb") as file:
        pickle.dump(ast, file)
    #print(syntax_tree)
    #tree_print(syntax_tree)
        