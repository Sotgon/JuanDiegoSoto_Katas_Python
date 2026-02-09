"""
PROYECTO LÓGICA: Katas de Python - SOLUCIONES COMPLETAS
"""

from functools import reduce
from typing import List, Tuple, Any

# ============================================================================
# EJERCICIO 1: Frecuencia de letras en una cadena
# ============================================================================
def frecuencia_letras(cadena: str) -> dict[str, int]:
    """
    Recibe una cadena y devuelve un diccionario con las frecuencias de cada letra.
    Los espacios no se consideran.
    """
    frecuencias = {}
    for letra in cadena:
        if letra != ' ':
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

# ============================================================================
# EJERCICIO 2: Doble de cada valor usando map()
# ============================================================================
def doble_valores(lista: List[int]) -> List[int]:
    """
    Dada una lista de números, devuelve una nueva lista con el doble de cada valor.
    """
    return list(map(lambda x: x * 2, lista))


# ============================================================================
# EJERCICIO 3: Palabras que contienen palabra objetivo
# ============================================================================
def palabras_con_objetivo(lista_palabras: List[str], palabra_objetivo: str) -> List[str]:
    """
    Devuelve lista de palabras que contienen la palabra objetivo.
    """
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]


# ============================================================================
# EJERCICIO 4: Diferencia entre dos listas usando map()
# ============================================================================
def diferencia_listas(lista1: List[float], lista2: List[float]) -> List[float]:
    """
    Calcula la diferencia entre los valores de dos listas.
    """
    return list(map(lambda x, y: x - y, lista1, lista2))


# ============================================================================
# EJERCICIO 5: Media y estado de aprobación
# ============================================================================
def calcular_media_estado(numeros: List[float], nota_aprobado: float = 5) -> Tuple[float, str]:
    """
    Calcula la media y determina si está aprobado o suspenso.
    """
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)


# ============================================================================
# EJERCICIO 6: Factorial recursivo
# ============================================================================
def factorial(n: int) -> int:
    """
    Calcula el factorial de un número de manera recursiva.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ============================================================================
# EJERCICIO 7: Lista de tuplas a lista de strings usando map()
# ============================================================================
def tuplas_a_strings(lista_tuplas: List[Tuple]) -> List[str]:
    """
    Convierte una lista de tuplas a una lista de strings.
    """
    return list(map(str, lista_tuplas))


# ============================================================================
# EJERCICIO 8: División con manejo de excepciones
# ============================================================================
def division_segura():
    """
    Pide dos números al usuario e intenta dividirlos con manejo de excepciones.
    """
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
        print(f"División exitosa: {num1} / {num2} = {resultado}")
    except ValueError:
        print("Error: Debes ingresar valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print(f"Error inesperado: {e}")


# ============================================================================
# EJERCICIO 9: Filtrar mascotas prohibidas usando filter()
# ============================================================================
def filtrar_mascotas_permitidas(mascotas: List[str]) -> List[str]:
    """
    Excluye mascotas prohibidas en España.
    """
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


# ============================================================================
# EJERCICIO 10: Promedio con excepción personalizada
# ============================================================================
class ListaVaciaError(Exception):
    """Excepción personalizada para lista vacía"""
    pass


def calcular_promedio(numeros: List[float]) -> float:
    """
    Calcula el promedio de una lista. Lanza excepción si está vacía.
    """
    try:
        if len(numeros) == 0:
            raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio")
        return sum(numeros) / len(numeros)
    except ListaVaciaError as e:
        print(f"Error: {e}")
        return None


# ============================================================================
# EJERCICIO 11: Validación de edad
# ============================================================================
def validar_edad():
    """
    Pide edad al usuario y valida que sea numérica y esté en rango válido.
    """
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120")
        print(f"Edad válida: {edad} años")
    except ValueError as e:
        print(f"Error: Edad no válida. {e}")


# ============================================================================
# EJERCICIO 12: Longitud de cada palabra usando map()
# ============================================================================
def longitud_palabras(frase: str) -> List[int]:
    """
    Devuelve una lista con la longitud de cada palabra.
    """
    palabras = frase.split()
    return list(map(len, palabras))


# ============================================================================
# EJERCICIO 13: Letras en mayúsculas y minúsculas sin repetir usando map()
# ============================================================================
def letras_mayus_minus(caracteres: str) -> List[Tuple[str, str]]:
    """
    Devuelve lista de tuplas con cada letra en mayúsculas y minúsculas sin repetir.
    """
    caracteres_unicos = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))


# ============================================================================
# EJERCICIO 14: Palabras que comienzan con letra específica usando filter()
# ============================================================================
def palabras_por_letra(palabras: List[str], letra: str) -> List[str]:
    """
    Retorna palabras que comienzan con una letra específica.
    """
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))


# ============================================================================
# EJERCICIO 15: Lambda que suma 3 a cada número
# ============================================================================
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))


# ============================================================================
# EJERCICIO 16: Palabras más largas que n usando filter()
# ============================================================================
def palabras_largas(texto: str, n: int) -> List[str]:
    """
    Devuelve palabras con longitud mayor que n.
    """
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


# ============================================================================
# EJERCICIO 17: Lista de dígitos a número usando reduce()
# ============================================================================
def digitos_a_numero(digitos: List[int]) -> int:
    """
    Convierte una lista de dígitos en un número.
    Ejemplo: [5,7,2] -> 572
    """
    return reduce(lambda acc, digito: acc * 10 + digito, digitos, 0)


# ============================================================================
# EJERCICIO 18: Filtrar estudiantes con calificación >= 90 usando filter()
# ============================================================================
def estudiantes_excelentes(estudiantes: List[dict]) -> List[dict]:
    """
    Filtra estudiantes con calificación mayor o igual a 90.
    """
    return list(filter(lambda est: est['calificacion'] >= 90, estudiantes))


# ============================================================================
# EJERCICIO 19: Lambda que filtra números impares
# ============================================================================
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))


# ============================================================================
# EJERCICIO 20: Filtrar solo valores int usando filter()
# ============================================================================
def solo_enteros(lista: List[Any]) -> List[int]:
    """
    Devuelve solo los valores de tipo int.
    """
    return list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), lista))


# ============================================================================
# EJERCICIO 21: Lambda que calcula el cubo
# ============================================================================
cubo = lambda x: x ** 3


# ============================================================================
# EJERCICIO 22: Producto total usando reduce()
# ============================================================================
def producto_total(numeros: List[float]) -> float:
    """
    Calcula el producto total de los valores.
    """
    return reduce(lambda acc, x: acc * x, numeros, 1)


# ============================================================================
# EJERCICIO 23: Concatenar palabras usando reduce()
# ============================================================================
def concatenar_palabras(palabras: List[str]) -> str:
    """
    Concatena una lista de palabras.
    """
    return reduce(lambda acc, palabra: acc + palabra, palabras, "")


# ============================================================================
# EJERCICIO 24: Diferencia total usando reduce()
# ============================================================================
def diferencia_total(numeros: List[float]) -> float:
    """
    Calcula la diferencia total restando todos los valores.
    """
    return reduce(lambda acc, x: acc - x, numeros)


# ============================================================================
# EJERCICIO 25: Contar caracteres
# ============================================================================
def contar_caracteres(texto: str) -> int:
    """
    Cuenta el número de caracteres en una cadena.
    """
    return len(texto)


# ============================================================================
# EJERCICIO 26: Lambda resto de división
# ============================================================================
resto_division = lambda x, y: x % y


# ============================================================================
# EJERCICIO 27: Promedio de lista
# ============================================================================
def promedio(numeros: List[float]) -> float:
    """
    Calcula el promedio de una lista de números.
    """
    return sum(numeros) / len(numeros) if numeros else 0


# ============================================================================
# EJERCICIO 28: Primer elemento duplicado
# ============================================================================
def primer_duplicado(lista: List[Any]) -> Any:
    """
    Busca y devuelve el primer elemento duplicado.
    """
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# ============================================================================
# EJERCICIO 29: Enmascarar caracteres excepto últimos 4
# ============================================================================
def enmascarar(variable: Any) -> str:
    """
    Convierte a string y enmascara todos los caracteres excepto los últimos 4.
    """
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]


# ============================================================================
# EJERCICIO 30: Verificar anagramas
# ============================================================================
def son_anagramas(palabra1: str, palabra2: str) -> bool:
    """
    Determina si dos palabras son anagramas.
    """
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


# ============================================================================
# EJERCICIO 31: Buscar nombre en lista
# ============================================================================
class NombreNoEncontradoError(Exception):
    """Excepción para nombre no encontrado"""
    pass


def buscar_nombre():
    """
    Solicita lista de nombres y busca un nombre específico.
    """
    try:
        nombres_input = input("Ingresa una lista de nombres separados por comas: ")
        nombres = [nombre.strip() for nombre in nombres_input.split(',')]
        
        nombre_buscar = input("Ingresa el nombre a buscar: ")
        
        if nombre_buscar in nombres:
            print(f"¡Nombre '{nombre_buscar}' encontrado en la lista!")
        else:
            raise NombreNoEncontradoError(f"El nombre '{nombre_buscar}' no está en la lista")
    except NombreNoEncontradoError as e:
        print(f"Error: {e}")


# ============================================================================
# EJERCICIO 32: Buscar empleado por nombre
# ============================================================================
def buscar_empleado(nombre_completo: str, empleados: List[dict[str, str]]) -> str:
    """
    Busca un empleado por nombre completo y devuelve su puesto.
    """
    for empleado in empleados:
        if empleado['nombre'] == nombre_completo:
            return empleado['puesto']
    return "Esta persona no trabaja aquí"


# ============================================================================
# EJERCICIO 33: Lambda que suma elementos de dos listas
# ============================================================================
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))


# ============================================================================
# EJERCICIO 34: Clase Arbol
# ============================================================================
class Arbol:
    """
    Clase que representa un árbol genérico con tronco y ramas.
    """
    def __init__(self):
        """Inicializa el árbol con tronco de longitud 1 y lista vacía de ramas."""
        self.tronco = 1
        self.ramas = []
    
    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.tronco += 1
    
    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1."""
        self.ramas.append(1)
    
    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas."""
        self.ramas = [rama + 1 for rama in self.ramas]
    
    def quitar_rama(self, posicion: int):
        """Elimina una rama en una posición específica."""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
    
    def info_arbol(self) -> dict[str, Any]:
        """Devuelve información sobre el árbol."""
        return {
            'longitud_tronco': self.tronco,
            'numero_ramas': len(self.ramas),
            'longitudes_ramas': self.ramas
        }


# ============================================================================
# EJERCICIO 36: Clase UsuarioBanco
# ============================================================================
class SaldoInsuficienteError(Exception):
    """Excepción para saldo insuficiente"""
    pass


class UsuarioBanco:
    """
    Representa a un usuario de banco con operaciones básicas.
    """
    def __init__(self, nombre: str, saldo: float, cuenta_corriente: bool):
        """Inicializa un usuario de banco."""
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    
    def retirar_dinero(self, cantidad: float):
        """Retira dinero del saldo."""
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(f"{self.nombre} no tiene saldo suficiente para retirar {cantidad}")
        self.saldo -= cantidad
    
    def transferir_dinero(self, otro_usuario: 'UsuarioBanco', cantidad: float):
        """Transfiere dinero desde otro usuario al usuario actual."""
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)
    
    def agregar_dinero(self, cantidad: float):
        """Agrega dinero al saldo."""
        self.saldo += cantidad


# ============================================================================
# EJERCICIO 37: Procesador de texto
# ============================================================================
def contar_palabras(texto: str) -> dict[str, int]:
    """Cuenta las palabras en un texto."""
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador


def reemplazar_palabras(texto: str, palabra_original: str, palabra_nueva: str) -> str:
    """Reemplaza una palabra por otra en el texto."""
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto: str, palabra: str) -> str:
    """Elimina una palabra del texto."""
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return ' '.join(palabras_filtradas)


def procesar_texto(texto: str, opcion: str, *args):
    """
    Procesa un texto según la opción especificada.
    Opciones: 'contar', 'reemplazar', 'eliminar'
    """
    if opcion == 'contar':
        return contar_palabras(texto)
    elif opcion == 'reemplazar':
        if len(args) >= 2:
            return reemplazar_palabras(texto, args[0], args[1])
        else:
            return "Error: faltan argumentos para reemplazar"
    elif opcion == 'eliminar':
        if len(args) >= 1:
            return eliminar_palabra(texto, args[0])
        else:
            return "Error: falta argumento para eliminar"
    else:
        return "Opción no válida"


# ============================================================================
# EJERCICIO 38: Determinar momento del día
# ============================================================================
def momento_del_dia(hora: int) -> str:
    """
    Determina si es noche, día o tarde según la hora (formato 24h).
    """
    if 6 <= hora < 12:
        return "día (mañana)"
    elif 12 <= hora < 20:
        return "tarde"
    else:
        return "noche"


# ============================================================================
# EJERCICIO 39: Calificación en texto
# ============================================================================
def calificacion_texto(nota: float) -> str:
    """
    Devuelve la calificación en texto según la nota numérica.
    """
    if 0 <= nota < 70:
        return "insuficiente"
    elif 70 <= nota < 80:
        return "bien"
    elif 80 <= nota < 90:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "nota inválida"


# ============================================================================
# EJERCICIO 40: Calcular área de figuras
# ============================================================================
def calcular_area(figura: str, datos: Tuple) -> float:
    """
    Calcula el área de una figura geométrica.
    - rectangulo: (base, altura)
    - circulo: (radio,)
    - triangulo: (base, altura)
    """
    import math
    
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        return None


# ============================================================================
# EJERCICIO 41: Programa de descuento en tienda
# ============================================================================
def programa_descuento():
    """
    Programa que calcula el precio final con descuento si aplica.
    """
    try:
        precio_original = float(input("Ingrese el precio original del artículo: "))
        
        tiene_cupon = input("¿Tiene un cupón de descuento? (sí/no): ").lower()
        
        if tiene_cupon == 'sí' or tiene_cupon == 'si':
            descuento = float(input("Ingrese el valor del cupón de descuento: "))
            
            if descuento > 0:
                precio_final = precio_original - descuento
                print(f"Descuento aplicado: {descuento}€")
                print(f"Precio final: {precio_final}€")
            else:
                print("Cupón no válido. El descuento debe ser mayor a cero.")
                print(f"Precio final (sin descuento): {precio_original}€")
        else:
            print(f"Precio final (sin descuento): {precio_original}€")
            
    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")


# ============================================================================
# EJEMPLOS DE USO Y PRUEBAS
# ============================================================================
if __name__ == "__main__":
    print("=" * 80)
    print("EJEMPLOS DE USO DE LAS SOLUCIONES")
    print("=" * 80)
    
    # Ejercicio 1
    print("\n1. Frecuencia de letras:")
    print(frecuencia_letras("hola mundo"))
    
    # Ejercicio 2
    print("\n2. Doble de valores:")
    print(doble_valores([1, 2, 3, 4, 5]))
    
    # Ejercicio 5
    print("\n5. Media y estado:")
    print(calcular_media_estado([6, 7, 8, 9]))
    
    # Ejercicio 6
    print("\n6. Factorial de 5:")
    print(factorial(5))
    
    # Ejercicio 17
    print("\n17. Dígitos a número:")
    print(digitos_a_numero([5, 7, 2]))
    
    # Ejercicio 34: Caso de uso Árbol
    print("\n34. Ejemplo Clase Arbol:")
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(1)
    print(arbol.info_arbol())
    
    # Ejercicio 36: Caso de uso UsuarioBanco
    print("\n36. Ejemplo Clase UsuarioBanco:")
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)
    print(f"Saldo Bob después de agregar 20: {bob.saldo}")
    try:
        alicia.transferir_dinero(bob, 80)
        print(f"Saldo Alicia después de recibir 80: {alicia.saldo}")
        print(f"Saldo Bob después de transferir 80: {bob.saldo}")
    except SaldoInsuficienteError as e:
        print(f"Error en transferencia: {e}")
    try:
        alicia.retirar_dinero(50)
        print(f"Saldo Alicia después de retirar 50: {alicia.saldo}")
    except SaldoInsuficienteError as e:
        print(f"Error al retirar: {e}")
    
    # Ejercicio 37: Caso de uso procesar_texto
    print("\n37. Ejemplo procesar_texto:")
    texto = "hola mundo hola"
    print("Contar:", procesar_texto(texto, 'contar'))
    print("Reemplazar:", procesar_texto(texto, 'reemplazar', 'hola', 'adiós'))
    print("Eliminar:", procesar_texto(texto, 'eliminar', 'hola'))
    
    print("\n" + "=" * 80)
    print("¡TODAS LAS SOLUCIONES IMPLEMENTADAS!")
    print("=" * 80)
