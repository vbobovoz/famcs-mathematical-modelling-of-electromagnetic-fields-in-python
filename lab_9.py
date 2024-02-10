# Реализовать класс для алгебраических полиномов одной переменной. В классе
# должны быть методы для сложения, вычитания, умножения двух полиномов, а
# также взятия производной. Лишние нулевые слагаемые должны удаляться.

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self._remove_zeros()

    def _remove_zeros(self):
        while len(self.coefficients) > 1 and self.coefficients[0] == 0:
            self.coefficients.pop(0)

    def __str__(self):
        result = ""
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    result += str(coef) + " + "
                elif 1 <= i < len(self.coefficients) - 1:
                    result += f"({coef} * X^{i}) + "
                if i == len(self.coefficients) - 1:
                    result += f"({coef} * X^{i})"
        return result if result else "0"

    def __add__(self, other):
        result = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        for i in range(max_len):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            result.append(coef1 + coef2)
        return Polynomial(result)

    def __sub__(self, other):
        result = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        for i in range(max_len):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            result.append(coef1 - coef2)
        return Polynomial(result)

    def __mul__(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result)

    def derivative(self):
        result = [i * coef for i, coef in enumerate(self.coefficients)][1:]
        return Polynomial(result)

if __name__ == "__main__":
    poly1 = Polynomial([1, 2, 3, 4, 5])
    poly2 = Polynomial([4, -2, 3, 6, 9, 0, 0, 2])

    print("Poly1:     ", poly1)
    print("Poly2:     ", poly2)
    print("Sum:       ", poly1 + poly2)
    print("Difference:", poly1 - poly2)
    print("Product:   ", poly1 * poly2)
    print("Derivative of Poly1: ", poly1.derivative())
    print("Derivative of Poly2: ", poly2.derivative())