import re
#Raúl Badillo Lora y Aldo Cova
#Analizador lexico del lenguaje BaCo

def lexer(input_str):

    TOKENS = [
    ('ESPACIO', r'\s+'),
    ('IPAREN', r'\('),
    ('DPAREN', r'\)'),
    ('NUMERO', r'-?\d+(\.\d+)?'),

    ('RESERVED',r'(PLUS|MINUS|MUL|DIV|EQUALS|ASSIGN|DIF|IF|AND|OR|PRINT|DEFINE)\s'),

    ('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9]*'),
    ('STRING', r'"[^"]*"'),
    ('QUOTE', r"'"),
    ('COMMENT', r';.*'),
]

    tokens = []
    i = 0
    while i < len(input_str):
        matched = False
        for token_type, pattern in TOKENS:
            match = re.match(pattern, input_str[i:])
            if match:
                value = match.group(0)
                if token_type != 'ESPACIO' and token_type != 'COMMENT':  # Ignore ESPACIO and comments
                    tokens.append((token_type, value))
                i += len(value)
                matched = True
                break
        if not matched:
            raise ValueError(f"Caracter no identificado: '{input_str[i]}' en posicion: {i}")
    return tokens

if __name__=='__main__':
    input_code = """(DEFINE (factorial eMULador)
                    (IF (EQUALS n 0)
                        1
                        (MUL n (factorial (MINUS n 1)))))"""
    tokens = lexer(input_code)
    for t in tokens:
        print(t)
