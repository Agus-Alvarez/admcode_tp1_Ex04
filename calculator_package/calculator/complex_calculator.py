"""
Cree un paquete de calculadora que contenga su clase

Cree un paquete de prueba que contenga el código de prueba para ese paquete o clase

Comentario en forma de docstring, en particular asociado a los diferentes métodos
"""

# calculator_package/
# ├── calculator/
# │   ├── __init__.py
# │   └── complex_calculator.py
# └── test/
#     ├── __init__.py
#     └── test_complex_calculator.py

# calculator_package/calculator/__init__.py

# calculator_package/calculator/complex_calculator.py
class SimpleComplexCalculator:
    """
    Calculadora de números complejos que realiza operaciones aritméticas básicas.
    
    Los números complejos se representan como listas de dos elementos [a, b]
    donde 'a' es la parte real y 'b' es la parte imaginaria.
        
    Example:
        >>> calc = SimpleComplexCalculator()
        >>> c1 = [1, 2]  # 1 + 2i
        >>> c2 = [3, 4]  # 3 + 4i
        >>> resultado = calc.sumar(c1, c2)
        >>> print(calc.formato_complejo(resultado))
        '4.00 + 6.00i'
    """
    
    def __init__(self):
        """Inicializa una nueva instancia de la calculadora."""
        pass
    
    def sumar(self, c1: list, c2: list) -> list:
        """
        Suma dos números complejos.
        
        Args:
            c1 (list): Primer número complejo en formato [real, imaginario]
            c2 (list): Segundo número complejo en formato [real, imaginario]
            
        Returns:
            list: Resultado de la suma en formato [real, imaginario]
            
        Example:
            >>> calc = SimpleComplexCalculator()
            >>> calc.sumar([1, 2], [3, 4])
            [4, 6]
        """
        return [c1[0] + c2[0], c1[1] + c2[1]]
    
    def restar(self, c1: list, c2: list) -> list:
        """
        Resta dos números complejos.
        
        Args:
            c1 (list): Primer número complejo en formato [real, imaginario]
            c2 (list): Segundo número complejo en formato [real, imaginario]
            
        Returns:
            list: Resultado de la resta en formato [real, imaginario]
            
        Example:
            >>> calc = SimpleComplexCalculator()
            >>> calc.restar([3, 4], [1, 2])
            [2, 2]
        """
        return [c1[0] - c2[0], c1[1] - c2[1]]
    
    def multiplicar(self, c1: list, c2: list) -> list:
        """
        Multiplica dos números complejos.
        
        La multiplicación se realiza según la fórmula:
        (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        
        Args:
            c1 (list): Primer número complejo en formato [real, imaginario]
            c2 (list): Segundo número complejo en formato [real, imaginario]
            
        Returns:
            list: Resultado de la multiplicación en formato [real, imaginario]
            
        Example:
            >>> calc = SimpleComplexCalculator()
            >>> calc.multiplicar([1, 2], [3, 4])
            [-5, 10]
        """
        real = c1[0] * c2[0] - c1[1] * c2[1]
        imaginario = c1[0] * c2[1] + c1[1] * c2[0]
        return [real, imaginario]
    
    def dividir(self, c1: list, c2: list) -> list:
        """
        Divide dos números complejos.
        
        La división se realiza multiplicando numerador y denominador por el conjugado
        del denominador y simplificando.
        
        Args:
            c1 (list): Numerador en formato [real, imaginario]
            c2 (list): Denominador en formato [real, imaginario]
            
        Returns:
            list: Resultado de la división en formato [real, imaginario]
            
        Raises:
            ValueError: Si el denominador es cero (c2[0]^2 + c2[1]^2 = 0)
            
        Example:
            >>> calc = SimpleComplexCalculator()
            >>> calc.dividir([3, 4], [1, -2])
            [-1, 2]
        """
        denominador = c2[0]**2 + c2[1]**2
        if denominador == 0:
            raise ValueError("No se puede dividir por cero")
        
        real = (c1[0] * c2[0] + c1[1] * c2[1]) / denominador
        imaginario = (c1[1] * c2[0] - c1[0] * c2[1]) / denominador
        return [real, imaginario]
    
    @staticmethod
    def formato_complejo(c: list) -> str:
        """
        Convierte un número complejo en su representación de texto.
        
        Args:
            c (list): Número complejo en formato [real, imaginario]
            
        Returns:
            str: Representación en formato 'a + bi' o 'a - bi'
            
        Example:
            >>> calc = SimpleComplexCalculator()
            >>> calc.formato_complejo([3.14, -2.718])
            '3.14 - 2.72i'
        """
        if c[1] >= 0:
            return f"{c[0]:.2f} + {c[1]:.2f}i"
        return f"{c[0]:.2f} - {abs(c[1]):.2f}i"