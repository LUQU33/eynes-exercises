import math

class Circle():
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0.")
        self._radius = radius
    
    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("El radio debe ser mayor que 0.")    
        self._radius = radius

    def get_area(self):
        return math.pi * (self._radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self._radius

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El valor ingresado debe ser mayor que 0.")
        return Circle(self._radius * n)

    def __str__(self):
        return f"""
        Radio: {self.get_radius()}
        Área: {round(self.get_area(), 2)}
        Perímetro: {round(self.get_perimeter(), 2)}
        """

# Primer circulo (antes de multiplicacion)
circulo = Circle(5)

# Segundo circulo, luego de la multiplicacion
circulo2 = circulo * 4

print(f"Información del primer círculo (pre multiplicación) {circulo}")

print(f"Información del segundo círculo (post multiplicación) {circulo2}")