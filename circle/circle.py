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
        return f"""INFO DEL CÍRCULO:
        Radio: {self.get_radius()}
        Área: {self.get_area()}
        Perímetro: {self.get_perimeter()}
        """

circulo = Circle(5)

print(circulo)