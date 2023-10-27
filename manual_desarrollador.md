## Manual para Desarrolladores del Analizador Léxico BaCo

### Introducción

Este código proporciona un analizador léxico para el lenguaje BaCo. Este analizador léxico identifica y categoriza diferentes tokens en una cadena de entrada basándose en patrones predefinidos.

### Autores
- Raúl Badillo Lora
- Aldo Cova

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
