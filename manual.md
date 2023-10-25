## Manual del Lenguaje BaCo

### Introducción:

BaCo es un lenguaje de programación inspirado en Lisp, caracterizado por su uso de paréntesis y su sintaxis de notación de prefijo. Es un lenguaje diseñado para operaciones matemáticas y manipulación de datos.

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

### Conclusión:

Con la capacidad de definir y llamar a funciones, BaCo se convierte en un lenguaje de programación mucho más poderoso y flexible. A través del uso de funciones, los usuarios pueden crear operaciones personalizadas y estructurar su código de manera más modular y reutilizable. ¡Disfruta programando en BaCo!