import sys
import json
import pickle
<<<<<<< HEAD
<<<<<<< HEAD
import networkx as nx
import matplotlib.pyplot as plt
=======
>>>>>>> 6a231a5 (falta actualizar el arbol y tabla de simbolos)


=======
import networkx as nx
import matplotlib.pyplot as plt
>>>>>>> 10c23e8 (update)

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
            raise ValueError(f"Token no esperado: {token_type}")

    def parse_list(index):
        children = []
        index += 1  # Saltarse el primer parentesis
        while tokens[index][0] != 'DPAREN':
            node, index = parse_expression(index)
            children.append(node)
        return Node('LIST', children=children), index + 1

    ast, _ = parse_expression(0)
    return ast

# Funcion para crear el arbol sintactico con parse


def tree_print(syntax_tree, level=0):
    print(' ' * level + syntax_tree.type)
    if syntax_tree.value is not None:
        print(' ' * (level) + syntax_tree.value)
    for child in syntax_tree.children:
        tree_print(child, level + 1)

# Funcion para crear el arbol sintactico con networkx y matplotlib


def tree_print_pickle(syntax_tree):
    G = nx.Graph()
    G.add_node(syntax_tree.type)
    if syntax_tree.value is not None:
        G.add_node(syntax_tree.value)
        G.add_edge(syntax_tree.type, syntax_tree.value)
    for child in syntax_tree.children:
        G.add_edge(syntax_tree.type, child.type)
        if child.value is not None:
            G.add_node(child.value)
            G.add_edge(child.type, child.value)
        tree_print_pickle(child)
    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == '__main__':
    # name = sys.argv[1:]
    tokens = []
    errors = []
    with open('table.json', "r") as file:
        lines = json.load(file)

    # print(lines)
    # Parse the tokens
    ast = parse(lines)
    print(ast)

    # Parse the tokens to build a syntax tree
    # syntax_tree = parser.parse()
    with open('syn_tree.pickle', "wb") as file:
        pickle.dump(ast, file)
    # print(syntax_tree)
    # tree_print(syntax_tree)

    # Generar el arbol sintactico con parse
    print("Arbol sintactico con parse")
    tree_print(ast)

    # Generar el arbol sintactico con networkx y matplotlib
    # print("Arbol sintactico con networkx y matplotlib")
    # tree_print_pickle(ast)
