from structures import LieAlgebra

# Example of a Lie algebra operations:
def complex_addition(a, b):
    return complex(a.real + b.real, a.imag + b.imag)

def complex_product(r, a):
    return complex(r * a.real, r * a.imag)

def complex_multiplication(a, b):
    return complex(a.real * b.real - a.imag * b.imag, a.real * b.imag + a.imag * b.real)

def lie_bracket(a, b):
    return complex_multiplication(a, b) - complex_multiplication(b, a)

# Example usage:
basis = [1j, 1]
algebra = LieAlgebra(basis, complex_addition, complex_product, complex_multiplication, lie_bracket)

a = 1j
b = 1
c = 2 + 2j
d = 3 - 1j

print(algebra.add(a, b))
print(algebra.product(2, c))
print(algebra.multiply(c, d))
print(algebra.lie_bracket(a, b))