import sys
import json
import pickle
from pars import Node


def actualizar_tasi(symbol_table, valor, nuevo):
    for item in symbol_table:
        if item[1] == valor:
            item[0] = nuevo


def buscar_tasi(symbol_table, valor):
    for item in symbol_table:
        if item[1] == valor:
            return item[0]
    return None


def actualizar_arbol(ast, valor, nuevo):
    if ast.value == valor:
        ast.type = nuevo

    for child in ast.children:
        actualizar_arbol(child, valor, nuevo)


def revisar_arbol(ast, symbol_table):
    tipo = buscar_tasi(symbol_table, ast.value)
    if tipo != None:
        ast.type = tipo

    for child in ast.children:
        revisar_arbol(child, symbol_table)


class SemanticError(Exception):
    pass


def analyze(ast):
    def analyze_node(node):
        if node.type == 'LIST':
            analyze_list(node)

    def analyze_list(node):
        print('analizando lista')
        if not node.children:
            raise SemanticError("Lista Vacía")

        first_child = node.children[0]
        print(first_child.value, first_child.type)
        if first_child.type == 'RESERVED':
            if first_child.value in ['PLUS ', 'MINUS ', 'MUL ', 'DIV ', 'EQUALS ', 'ASSIGN ', 'DIF ', 'IF ', 'AND ', 'OR ']:
                analyze_math_operator(node.children)
            if first_child.value == 'DEFINE ':
                analyze_define(node.children)
        if first_child.type == 'FUNCION':
            analyze_funcion(node.children)

    def analyze_math_operator(children):
        print('analizando operador')
        if len(children) < 3:
            raise SemanticError(
                "Los operadores requieren al menos dos operandos")
        for child in children[1:]:
            if child.type != 'NUMERO':
                if child.type == 'IDENTIFIER':
                    child.type = 'NUMERO'
                    # actualizar_arbol(child, child.value, 'NUMERO')
                    actualizar_tasi(symbol_table, child.value, 'NUMERO')

                elif child.type == 'LIST':
                    analyze_list(child)
                else:
                    raise SemanticError(
                        "Tipo de operador no valido")

    def analyze_define(children):
        print('analizando DEFINE')
        if len(children) != 4:
            raise SemanticError("DEFINE requiere al menos dos argumentos")
        if children[1].type != 'IDENTIFIER':
            raise SemanticError(
                "Primer argumento de DEFINE debe de ser un identificador")
        children[1].type = 'FUNCION'
        # actualizar_arbol(children[3], children[1].value, 'FUNCION')
        actualizar_tasi(symbol_table, children[1].value, 'FUNCION')
        analyze_node(children[3])

    def analyze_funcion(children):
        print('analizando funcion')
        if len(children) != 2:
            raise SemanticError("Las funciones requieren un argumento")
        if children[1].type == 'LIST':
            analyze_list(children[1])

    analyze_node(ast)


if __name__ == '__main__':
    # ast = Node()
    with open('syn_tree.pickle', "rb") as file:
        ast = pickle.load(file)
    # print(ast)

    with open('table.json', "r") as file:
        symbol_table = json.load(file)
    try:
        analyze(ast)
        # print(ast)
        print("Analisis semantico completado exitosamente.")
        print(symbol_table)
        revisar_arbol(ast, symbol_table)
        print(ast)
    except SemanticError as e:
        print(f"Error semantico: {e}")
