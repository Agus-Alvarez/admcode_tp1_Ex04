# calculator_package/test/test_complex_calculator.py

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from calculator_package.calculator.complex_calculator import SimpleComplexCalculator

def test_calculadora():
    """
    Función principal de pruebas para la calculadora de números complejos.
    Ejecuta todas las pruebas y muestra los resultados.
    """
    # Crear una instancia de la calculadora
    calc = SimpleComplexCalculator()
    
    # Números complejos de prueba
    complejo1 = [4.67, 5.89]  # 4.67 + 5.89i
    complejo2 = [2.0, 3.0]    # 2 + 3i
    
    print("=== Pruebas de la Calculadora de Números Complejos ===")
    print(f"Número complejo 1: {calc.formato_complejo(complejo1)}")
    print(f"Número complejo 2: {calc.formato_complejo(complejo2)}")
    print("\nEjecutando pruebas...")
    
    # Prueba de suma
    suma = calc.sumar(complejo1, complejo2)
    print("\n1. Prueba de suma:")
    print(f"Resultado esperado: 6.67 + 8.89i")
    print(f"Resultado obtenido: {calc.formato_complejo(suma)}")
    print("Prueba exitosa" if abs(suma[0] - 6.67) < 0.01 and abs(suma[1] - 8.89) < 0.01 
          else "Prueba fallida")
    
    # Prueba de resta
    resta = calc.restar(complejo1, complejo2)
    print("\n2. Prueba de resta:")
    print(f"Resultado esperado: 2.67 + 2.89i")
    print(f"Resultado obtenido: {calc.formato_complejo(resta)}")
    print("Prueba exitosa" if abs(resta[0] - 2.67) < 0.01 and abs(resta[1] - 2.89) < 0.01 
          else "Prueba fallida")
    
    # Prueba de multiplicación
    producto = calc.multiplicar(complejo1, complejo2)
    real_esperado = 4.67 * 2.0 - 5.89 * 3.0
    imag_esperado = 4.67 * 3.0 + 5.89 * 2.0
    print("\n3. Prueba de multiplicación:")
    print(f"Resultado esperado: {real_esperado:.2f} + {imag_esperado:.2f}i")
    print(f"Resultado obtenido: {calc.formato_complejo(producto)}")
    print("Prueba exitosa" if abs(producto[0] - real_esperado) < 0.01 
          and abs(producto[1] - imag_esperado) < 0.01 else "Prueba fallida")
    
    # Prueba de división
    division = calc.dividir(complejo1, complejo2)
    denominador = complejo2[0]**2 + complejo2[1]**2
    real_esperado = (complejo1[0] * complejo2[0] + complejo1[1] * complejo2[1]) / denominador
    imag_esperado = (complejo1[1] * complejo2[0] - complejo1[0] * complejo2[1]) / denominador
    print("\n4. Prueba de división:")
    print(f"Resultado esperado: {real_esperado:.2f} + {imag_esperado:.2f}i")
    print(f"Resultado obtenido: {calc.formato_complejo(division)}")
    print("Prueba exitosa" if abs(division[0] - real_esperado) < 0.01 
          and abs(division[1] - imag_esperado) < 0.01 else "Prueba fallida")
    
    # Prueba de división por cero
    print("\n5. Prueba de división por cero:")
    try:
        calc.dividir(complejo1, [0, 0])
        print("Prueba fallida: No se detectó el error de división por cero")
    except ValueError as e:
        print(f"Prueba exitosa: {e}")
    
    # Prueba de formato
    print("\n6. Pruebas de formato:")
    numero_positivo = [1.23, 4.56]
    numero_negativo = [1.23, -4.56]
    print("6.1 Número con parte imaginaria positiva:")
    print(f"Resultado esperado: 1.23 + 4.56i")
    print(f"Resultado obtenido: {calc.formato_complejo(numero_positivo)}")
    print("Prueba exitosa" if calc.formato_complejo(numero_positivo) == "1.23 + 4.56i" 
          else "Prueba fallida")
    
    print("\n6.2 Número con parte imaginaria negativa:")
    print(f"Resultado esperado: 1.23 - 4.56i")
    print(f"Resultado obtenido: {calc.formato_complejo(numero_negativo)}")
    print("Prueba exitosa" if calc.formato_complejo(numero_negativo) == "1.23 - 4.56i" 
          else "Prueba fallida")

if __name__ == '__main__':
    test_calculadora()