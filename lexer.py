import re
import sys
#Raúl Badillo Lora y Aldo Cova
#Analizador lexico del lenguaje BaCo

def lexer(input_str,linea):

    TOKENS = [
    ('ESPACIO', r'\s+'),

    ('IPAREN', r'\('),
    ('DPAREN', r'\)'),
    ('NUMERO', r'-?\d+(\.\d+)?'),

    ('RESERVED',r'(PLUS|MINUS|MUL|DIV|EQUALS|ASSIGN|DIF|IF|AND|OR|PRINT|DEFINE)\s'),

    ('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9]*'),
    ('STRING', r'"[^"]*"'),
    ('COMMENT', r';.*'),
]

    tokens = []
    errors = []
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
            print(f"Caracter no identificado: '{input_str[i]}' en linea: {linea}")
            errors.append((input_str[i],linea))
            i+=1
    return tokens, errors

if __name__=='__main__':
    name = sys.argv[1:]
    tokens =[]
    errors =[]
    with open (name[0],"r") as file:
        nl=0
        
        for line in file:
            input_code=line
            temp_tokens, temp_errors=lexer(input_code,nl)
            tokens+=temp_tokens
            errors+=temp_errors
            nl+=1
    for i in tokens:
        print(i)
    with open ("table.tasi", "w") as file:
        file.write(str(tokens))
    with open ("error.tarro", "w") as file:
        file.write(str(errors))
