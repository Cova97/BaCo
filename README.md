## Manual del Lenguaje BaCo

### Introducción:

BaCo es un lenguaje de programación caracterizado por su uso de paréntesis y su sintaxis de notación de prefijo. Tiene la capacidad de definir funciones, lo cual le da mucha flexibilidad. Es un lenguaje minimalista de propósito general.

Lee archivos de extensión `.baco`. El nombre del lenguaje proviene de las iniciales de sus creadores: **Ba**dillo **Co**va



### Sintaxis Básica:

1. **Expresiones**: En BaCo, todo está representado como una expresión. Las operaciones están en notación de prefijo, es decir, el operador se coloca antes de sus operandos.
   
   Ejemplo:
   ```
   (PLUS 3 4)   ; Suma 3 + 4
   ```

2. **Comentarios**: Todo lo que sigue a un punto y coma (`;`) hasta el final de la línea es considerado un comentario y es ignorado por el analizador.
   
   Ejemplo:
   ```
   ; Esto es un comentario
   ```

3. **Números**: Los números pueden ser enteros o decimales.
   
   Ejemplo:
   ```
   123
   -456
   78.9
   ```

4. **Identificadores**: Los identificadores son secuencias de letras y números que comienzan con una letra.
   
   Ejemplo:
   ```
   x
   variable1
   ```

5. **Palabras Reservadas**: Estas son las palabras especiales que tienen significados específicos en BaCo. No deben ser utilizadas como identificadores.
   
   - Operaciones aritméticas: PLUS, MINUS, MUL, DIV
   - Comparadores: EQUALS, DIF
   - Lógica: AND, OR
   - Otros: IF, PRINT, DEFINE, ASSIGN

6. **Strings**: Las cadenas de caracteres están encerradas entre comillas dobles.
   
   Ejemplo:
   ```
   "Esto es una cadena"
   ```

### Ejemplos de Expresiones:

1. **Operaciones Aritméticas**:
   ```
   (PLUS 3 5)      ; Resulta en 8
   (MINUS 9 4)     ; Resulta en 5
   (MUL 3 7)       ; Resulta en 21
   (DIV 8 2)       ; Resulta en 4
   ```

2. **Operaciones Lógicas**:
   ```
   (AND 0 1)    ; Resulta en 0
   (OR 1 0)     ; Resulta en 1
   ```

3. **Condicional**:
   ```
   (IF (EQUALS 5 5) 
       (PRINT "Son iguales") 
       (PRINT "Son diferentes"))
   ```

4. **Definición y Asignación**:
   ```
   (DEFINE (sumar a b)
    (PLUS a b))        ; Define una función que suma el valor a y b
   (ASSIGN x 20)        ; Asigna el valor 20 a x
   ```



### Llamada a Funciones:

Para llamar a una función, simplemente escribe su nombre seguido de sus argumentos.

Ejemplo:

```
(sumar 3 4)  ; Llama a la función 'sumar' con los argumentos 3 y 4
```

Este ejemplo llamará a la función `sumar` definida anteriormente y devolverá el valor 7.



## Manual para Desarrolladores del Analizador Léxico BaCo

### Introducción

Este código proporciona un analizador léxico para el lenguaje BaCo. Este analizador léxico identifica y categoriza diferentes tokens en una cadena de entrada basándose en patrones predefinidos.

### Autores
- Raúl Badillo Lora
- Aldo Cova Martínez

### Funciones

#### `lexer(input_str,linea)`
Esta función toma una cadena de entrada `input_str` y un número de línea `linea`. Retorna una lista de tokens identificados y una lista de posibles errores encontrados durante el análisis.

- **Parámetros**:
  - `input_str` (str): Cadena de texto que será analizada.
  - `linea` (int): Número de línea que está siendo analizada (utilizada para reportar errores).

- **Retorno**: 
  - Dos listas: `tokens` y `errors`. La lista `tokens` contiene tuplas de tokens identificados. La lista `errors` contiene errores identificados.

#### Lista `TOKENS`
Contiene las expresiones regulares de los tokens que se reconocen en el lenguaje. Cada token está representado como una tupla de dos elementos, donde el primer elemento es el nombre del token y el segundo elemento es la expresión regular que coincide con el token.

#### Ejecución Principal

Cuando el script se ejecuta como programa principal (`__name__=='__main__'`), realiza lo siguiente:

1. Lee el nombre del archivo desde la línea de comandos.
2. Abre el archivo y analiza línea por línea utilizando la función `lexer`.
3. Imprime los tokens identificados en la consola.
4. Escribe los tokens identificados en un archivo llamado `table.tasi`.
5. Escribe los errores identificados en un archivo llamado `error.tarro`.

### Uso

Para usar este analizador léxico, ejecute el script desde la línea de comandos y proporcione el nombre del archivo que desea analizar como argumento. Por ejemplo:

```
python lexer.py archivo_a_analizar.baco
```

### Salida

El programa genera dos archivos:

1. `table.tasi`: Contiene una representación de lista de los tokens identificados.
2. `error.tarro`: Contiene una representación de lista de los errores identificados.

### Notas

- Si un carácter en la entrada no coincide con ninguno de los patrones definidos, se considera un error y se añade a la lista de errores.
- Los tokens de tipo `ESPACIO` y `COMMENT` son ignorados y no se agregan a la lista de tokens.

## Manual para Desarrolladores del Analizador Sintáctico BaCo

### Introducción

Este código implementa un analizador sintáctico para el lenguaje BaCo. El analizador sintáctico toma una lista de tokens generada por el analizador léxico y construye un Árbol de Sintaxis Abstracta (AST) que representa la estructura sintáctica del programa.

### Clases y Funciones

#### Clase `Node`
Representa un nodo en el AST.

- **Atributos**:
  - `type`: Tipo del nodo (por ejemplo, 'IDENTIFIER', 'NUMERO', 'LIST').
  - `value`: El valor del token, si corresponde.
  - `children`: Una lista de nodos hijos en el AST.

- **Método `__repr__`**:
  - Proporciona una representación en cadena del nodo para propósitos de depuración.

#### Función `parse(tokens)`
Esta función construye el AST a partir de la lista de tokens.

- **Parámetros**:
  - `tokens`: Una lista de tokens (tuplas) generada por el analizador léxico.

- **Retorno**: 
  - Un objeto `Node` que representa la raíz del AST.

#### Funciones Auxiliares Internas
- `parse_expression(index)`: Analiza una expresión a partir de un índice dado en la lista de tokens.
- `parse_list(index)`: Analiza una lista de expresiones (delimitadas por paréntesis) y construye un nodo de tipo 'LIST'.

### Proceso de Análisis Sintáctico

1. **Inicio del Análisis**: Comienza llamando a `parse_expression` con el índice 0.
2. **Análisis de Expresiones y Listas**:
   - Si el token es un paréntesis de apertura ('IPAREN'), se llama a `parse_list`.
   - Si el token es un número, identificador, cadena o reservado, se crea un nodo con su tipo y valor.
   - Si encuentra un token inesperado, lanza una excepción `ValueError`.
3. **Construcción del AST**: Cada llamada a `parse_expression` o `parse_list` retorna un nodo y el índice del próximo token a analizar.

### Uso

El analizador sintáctico depende de la salida del analizador léxico. Asegúrese de que tiene una lista de tokens válida (como la producida por el analizador léxico BaCo) antes de llamar a `parse(tokens)`.

### Salida

El resultado es un objeto `Node` que sirve como raíz del AST. Este árbol puede ser utilizado para análisis semántico, generación de código, o cualquier otro propósito relacionado con el procesamiento de lenguajes.

### Notas

- El análisis se realiza de manera recursiva, lo que facilita el manejo de estructuras anidadas.

## Manual para Desarrolladores del Analizador Semántico BaCo

### Introducción

Este código implementa un analizador semántico para el lenguaje BaCo. El analizador semántico trabaja sobre el Árbol de Sintaxis Abstracta (AST) generado por el analizador sintáctico y utiliza una tabla de símbolos para verificar la corrección semántica del programa.

### Funciones Principales

#### `actualizar_tasi(symbol_table, valor, nuevo)`
Actualiza la tabla de símbolos.

- **Parámetros**:
  - `symbol_table`: Tabla de símbolos actual.
  - `valor`: Valor a buscar en la tabla.
  - `nuevo`: Nuevo tipo para actualizar en la tabla.

#### `buscar_tasi(symbol_table, valor)`
Busca un valor en la tabla de símbolos y retorna su tipo.

- **Parámetros**:
  - `symbol_table`: Tabla de símbolos.
  - `valor`: Valor a buscar.
- **Retorno**:
  - Tipo del símbolo buscado, o `None` si no se encuentra.

#### `actualizar_arbol(ast, valor, nuevo)`
Actualiza los tipos en el AST.

- **Parámetros**:
  - `ast`: Árbol de Sintaxis Abstracta.
  - `valor`: Valor a buscar en el AST.
  - `nuevo`: Nuevo tipo para actualizar en el AST.

#### `revisar_arbol(ast, symbol_table)`
Revisa y actualiza el AST según la tabla de símbolos.

- **Parámetros**:
  - `ast`: Árbol de Sintaxis Abstracta.
  - `symbol_table`: Tabla de símbolos.

#### `analyze(ast)`
Analiza el AST para verificar la corrección semántica.

- **Parámetros**:
  - `ast`: Árbol de Sintaxis Abstracta.

### Proceso de Análisis Semántico

1. **Análisis de Nodos**: `analyze` recorre el AST y delega el análisis de cada nodo según su tipo.
2. **Análisis de Listas**: `analyze_list` gestiona las listas de nodos, verificando su corrección semántica.
3. **Operadores Matemáticos**: `analyze_math_operator` verifica la correcta utilización de operadores matemáticos.
4. **Definiciones (DEFINE)**: `analyze_define` maneja la correcta definición de funciones o variables.
5. **Funciones**: `analyze_funcion` verifica el uso correcto de las funciones.

### Excepciones

El código lanza la excepción `SemanticError` cuando encuentra errores semánticos, como el uso incorrecto de tipos o estructuras.

### Uso

Para usar este analizador semántico:

1. Asegúrese de tener un AST válido y una tabla de símbolos generada por el analizador léxico y sintáctico.
2. Llame a `analyze(ast)` con el AST como argumento.

### Salida

El análisis semántico actualiza el AST y la tabla de símbolos para reflejar los tipos correctos de los nodos y símbolos. Si se encuentra un error semántico, se lanza una excepción `SemanticError` con detalles del error.
