from structures import Element, Ring

# Example of a ring operations:
def integer_addition(a, b):
    return a + b

def integer_multiplication(a, b):
    return a * b

# Example usage:
elements = [Element(i) for i in range(5)]
ring = Ring(elements, integer_addition, integer_multiplication)

print(ring.add(2, 3))
print(ring.multiply(2, 3))