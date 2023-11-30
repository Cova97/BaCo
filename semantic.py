import sys
import json
import pickle
from pars import Node


def actualizar_tasi(symbol_table, valor, nuevo):
    for item in symbol_table:
        if item[1] == valor:
            item[0] = nuevo



def actualizar_arbol(ast, valor, nuevo):
    if ast.value==valor:
        ast.type = nuevo
    
    for child in ast.children:
        actualizar_arbol(child, valor, nuevo)
    
    
    

class SemanticError(Exception):
    pass

def analyze(ast):
    def analyze_node(node):
        if node.type == 'LIST':
            analyze_list(node)

    def analyze_list(node):
        print('analizando lista')
        if not node.children:
            raise SemanticError("Empty list")

        first_child = node.children[0]
        print(first_child.value, first_child.type)
        if first_child.type == 'RESERVED':
            if first_child.value in ['PLUS ','MINUS ','MUL ','DIV ','EQUALS ','ASSIGN ','DIF ','IF ','AND ','OR ']:
                analyze_math_operator(node.children)
            if first_child.value == 'DEFINE ':
                analyze_define(node.children)
        if first_child.type =='FUNCION':
            analyze_funcion(node.children)
            

    def analyze_math_operator(children):
        print('analizando operador')
        if len(children) < 3:  
            raise SemanticError("Math operator requires at least two operands")
        for child in children[1:]:
            if child.type != 'NUMERO':
                if child.type == 'IDENTIFIER':
                    child.type ='NUMERO'
                    
                elif child.type =='LIST':
                    analyze_list(child)
                else:
                    raise SemanticError("Math operator requires numeric operands")

    def analyze_define(children):
        print('analizando DEFINE')
        if len(children) != 4:
            raise SemanticError("Define requires three arguments")
        if children[1].type != 'IDENTIFIER':
            raise SemanticError("First argument of define must be a symbol")
        children[1].type = 'FUNCION'
        analyze_node(children[3])
        
        
    def analyze_funcion(children):
        print('analizando funcion')
        if len(children) != 2:
            raise SemanticError("Las funciones requieren un argumento")
        if children[1].type=='LIST':
            analyze_list(children[1])

    analyze_node(ast)


if __name__=='__main__':
    #ast = Node()
    with open('syn_tree.pickle', "rb") as file:
        ast = pickle.load(file)
    #print(ast)
        
    with open('table.json', "r") as file:
        symbol_table = json.load(file)
# Perform semantic analysis
    try:
        analyze(ast)
        print(ast)
        print("Analisis semantico completado exitosamente.")
    except SemanticError as e:
        print(f"Semantic error: {e}")
