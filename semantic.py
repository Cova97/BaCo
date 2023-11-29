import sys
import json
import pickle
from pars import Node

class SemanticError(Exception):
    pass


def infer_type(node, context):
    if node.type == 'NUMERO':
        return 'NUMERO'
    elif node.type == 'STRING':
        return 'STRING'
    elif node.type == 'SYMBOL':
        # In a real implementation, the type would come from the variable's declaration
        print(context['variables'].get(node.value, 'unknown'))
        return context['variables'].get(node.value, 'unknown')
    elif node.type == 'LIST':
        return analyze_expression_type(node, context)
    else:
        return 'unknown'


def analyze_expression_type(node, context):
    if not node.children:
        raise SemanticError("Empty expression")

    first = node.children[0]
    if first.type != 'IDENTIFIER':
        raise SemanticError("Invalid expression")

    if first.value == 'DEFINE':
        return analyze_define_type(node, context)
    if first.value in ['PLUS','MINUS','MUL','DIV','EQUALS','ASSIGN','DIF','IF','AND','OR']:  # Arithmetic operators
        return check_arithmetic_operands(node.children[1:], context)
    # Add more cases for other operators or functions


def analyze_define_type(node, context):
    if len(node.children) < 3:
        raise SemanticError("Incorrect NUMERO of arguments to 'define'")

    identifier = node.children[1]
    if identifier.type == 'SYMBOL':  # Variable definition
        value_node = node.children[2]
        value_type = infer_type(value_node, context)
        context['variables'][identifier.value] = value_type
        return value_type
    elif identifier.type == 'LIST':  # Function definition
        # For a function, you might return a 'function' type or more detailed type information
        return 'function'
    else:
        raise SemanticError(
            "'define' first argument must be a symbol or a list for function definitions")


def check_arithmetic_operands(operands, context):
    if not operands:
        raise SemanticError("Arithmetic operation requires operands")
    for operand in operands:
        operand_type = infer_type(operand, context)
        if operand_type == 'unknown':
            context['variables'][operand.value] = 'NUMERO'
            operand_type = 'NUMERO'
        if operand_type != 'NUMERO':
            raise SemanticError(
                f"Arithmetic operations require numeric operands, found {operand, operand_type}")
    print(context)
    return 'NUMERO'


def semantic_analysis(node, context=None):
    if context is None:
        context = {'functions': set(), 'variables': {}}
    node.type = infer_type(node, context)
    if node.type == 'LIST':
        if not node.children:
            raise SemanticError("Empty list found")
        # Check the first element to determine the type of expression
        first = node.children[0]
        if first.type == 'IDENTIFIER':
            if first.value == 'define':
                return analyze_define(node, context)
            elif first.value == 'if':
                return analyze_if(node, context)
            elif first.value in context['functions']:
                return analyze_function_call(node, context)
            else:
                raise SemanticError(
                    f"Unknown function or special form: {first.value}")
        else:
            for child in node.children:
                semantic_analysis(child, context)

    elif node.type == 'IDENTIFIER':
        if node.value not in context['variables']:
            raise SemanticError(f"Undefined variable: {node.value}")

    elif node.type in ['NUMERO', 'STRING', 'unknown']:
        pass  # No further analysis needed for literals

    else:
        raise SemanticError(f"Unexpected node type: {node, node.type}")
    print(context)


def analyze_define(node, context):
    if len(node.children) != 4:
        raise SemanticError(
            f"Incorrect NUMERO of arguments to 'define' {len(node.children)}")
    identifier = node.children[1]
    inp = node.children[2]
    if identifier.type != 'IDENTIFIER':
        raise SemanticError(
            f"'define' first argument must be a symbol instead of{identifier.type}")
    if inp.type != 'IDENTIFIER':
        raise SemanticError(
            f"'define' second argument must be a symbol instead of{identifier.type}")
    context['variables'][inp.value] = 'unknown'
    context['functions'].add(identifier.value)
    semantic_analysis(node.children[3], context)


def analyze_if(node, context):
    if len(node.children) != 4:
        raise SemanticError("Incorrect NUMERO of arguments to 'if'")
    for part in node.children[1:]:
        semantic_analysis(part, context)


def analyze_assign(node, context):
    if len(node.children) != 3:
        raise SemanticError("Incorrect NUMERO of arguments to '='")
    identifier = node.children[1]
    if identifier.type != 'IDENTIFIER':
        raise SemanticError(
            f"'define' first argument must be a symbol instead of{identifier.type}")
    semantic_analysis(node.children[2], context)
    context['variables'][node.children[1].value] = node.children[2].type


def analyze_math(node, context):
    if len(node.children) != 3:
        raise SemanticError("Incorrect NUMERO of arguments")
    identifier = node.children[1]
    if (node.children[1] != 'NUMERO') or (node.children[2] != 'NUMERO'):
        raise SemanticError(
            f"Espera tipo NUMERO en vez de {identifier.type}")
    context['variables'].add(identifier.value)
    semantic_analysis(node.children[2], context)


def analyze_function_call(node, context):
    # Additional checks can be added here for specific function calls
    for arg in node.children[1:]:
        semantic_analysis(arg, context)






if __name__=='__main__':
    #ast = Node()
    with open('syn_tree.pickle', "rb") as file:
        ast = pickle.load(file)
    print(ast)
        
    with open('table.json', "r") as file:
        symbol_table = json.load(file)

    
    context = {'functions': set(), 'variables': {}}
# Perform semantic analysis
    try:
        semantic_analysis(ast, context)
        print(ast, context)
        print("Analisis semantico completado exitosamente.")
    except SemanticError as e:
        print(f"Semantic error: {e}")
