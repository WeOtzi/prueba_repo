#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejemplo simple para el repositorio de prueba.
"""

def saludar(nombre):
    """
    Función que devuelve un saludo personalizado.
    
    Args:
        nombre (str): Nombre de la persona a saludar
        
    Returns:
        str: Saludo personalizado
    """
    return f"¡Hola, {nombre}! Bienvenido al repositorio de prueba."

def main():
    """Función principal del programa."""
    nombre = input("Por favor, introduce tu nombre: ")
    mensaje = saludar(nombre)
    print(mensaje)
    
if __name__ == "__main__":
    main() 