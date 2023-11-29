import re

# Define token types and their regular expressions
TOKENS = [
    ('WHITESPACE', r'\s+'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('NUMBER', r'-?\d+(\.\d+)?'),
    ('SYMBOL', r'[a-zA-Z\-+*/=][a-zA-Z0-9\-+*/_]*'),
    ('STRING', r'"[^"]*"'),
    ('QUOTE', r"'"),
    ('COMMENT', r';.*'),
]


def lexer(input_str):
    tokens = []
    i = 0
    while i < len(input_str):
        matched = False
        for token_type, pattern in TOKENS:
            match = re.match(pattern, input_str[i:])
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE' and token_type != 'COMMENT':  # Ignore whitespace and comments
                    tokens.append((token_type, value))
                i += len(value)
                matched = True
                break
        if not matched:
            raise ValueError(
                f"Unexpected character '{input_str[i]}' at position {i}")
    return tokens


# Test
input_code = """(define factorial n (if (= n 0) 1 (* n (factorial (- n 1)))))"""
tokens = lexer(input_code)
for t in tokens:
    print(t)


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
        if token_type == 'LPAREN':
            return parse_list(index)
        elif token_type in ['NUMBER', 'SYMBOL', 'STRING']:
            return Node(token_type, token_value), index + 1
        else:
            raise ValueError(f"Unexpected token: {token_type}")

    def parse_list(index):
        children = []
        index += 1  # Skip the opening parenthesis
        while tokens[index][0] != 'RPAREN':
            node, index = parse_expression(index)
            children.append(node)
        return Node('LIST', children=children), index + 1

    ast, _ = parse_expression(0)
    return ast


# Parse the tokens
ast = parse(tokens)
print(ast)


class SemanticError(Exception):
    pass

math_functions = {'+','-','*','/'}

def semantic_analysis(node, context=None):
    if context is None:
        context = {'functions': set(), 'variables': set()}

    if node.type == 'LIST':
        if not node.children:
            raise SemanticError("Empty list found")
        # Check the first element to determine the type of expression
        first = node.children[0]
        if first.type == 'SYMBOL':
            if first.value == 'define':
                return analyze_define(node, context)
            elif first.value == 'if':
                return analyze_if(node, context)
            elif first.value == '=':
                return analyze_assign(node, context)
            elif first.value in math_functions:
                return analyze_math(node, context)
            elif first.value in context['functions']:
                return analyze_function_call(node, context)
            else:
                raise SemanticError(
                    f"Unknown function or special form: {first.value}")
        else:
            for child in node.children:
                semantic_analysis(child, context)

    elif node.type == 'SYMBOL':
        if node.value not in context['variables']:
            raise SemanticError(f"Undefined variable: {node.value}")

    elif node.type in ['NUMBER', 'STRING']:
        pass  # No further analysis needed for literals

    else:
        raise SemanticError(f"Unexpected node type: {node.type}")


def analyze_define(node, context):
    if len(node.children) != 4:
        raise SemanticError(
            f"Incorrect number of arguments to 'define' {len(node.children)}")
    identifier = node.children[1]
    inp = node.children[2]
    if identifier.type != 'SYMBOL':
        raise SemanticError(
            f"'define' first argument must be a symbol instead of{identifier.type}")
    if inp.type != 'SYMBOL':
        raise SemanticError(
            f"'define' second argument must be a symbol instead of{identifier.type}")
    context['variables'].add(inp.value)
    context['functions'].add(identifier.value)
    semantic_analysis(node.children[3], context)


def analyze_if(node, context):
    if len(node.children) != 4:
        raise SemanticError("Incorrect number of arguments to 'if'")
    for part in node.children[1:]:
        semantic_analysis(part, context)


def analyze_assign(node, context):
    if len(node.children) != 3:
        raise SemanticError("Incorrect number of arguments to '='")
    identifier = node.children[1]
    if identifier.type != 'SYMBOL':
        raise SemanticError(
            f"'define' first argument must be a symbol instead of{identifier.type}")
    context['variables'].add(identifier.value)
    semantic_analysis(node.children[2], context)
    
def analyze_math(node, context):
    if len(node.children) != 3:
        raise SemanticError("Incorrect number of arguments")
    identifier = node.children[1]
    if (node.children[1] != 'NUMBER') or (node.children[2] != 'NUMBER'):
        raise SemanticError(
            f"function exp{identifier.type}")
    context['variables'].add(identifier.value)
    semantic_analysis(node.children[2], context)
    

def analyze_function_call(node, context):
    # Additional checks can be added here for specific function calls
    for arg in node.children[1:]:
        semantic_analysis(arg, context)


# Perform semantic analysis
try:
    semantic_analysis(ast)
    print("Semantic analysis completed successfully.")
except SemanticError as e:
    print(f"Semantic error: {e}")
