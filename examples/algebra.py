from structures import Element, Algebra

# Example of an algebra operations:
def vector_addition(a, b):
    return [x + y for x, y in zip(a, b)]

def scalar_product(r, a):
    return [r * x for x in a]

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def cross_product(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

# Example usage:
dimension_size = 5
basis = [Element([1 if i == j else 0 for j in range(dimension_size)]) for i in range(dimension_size)]
algebra = Algebra(basis, vector_addition, scalar_product, dot_product)

print(algebra.add([0, 1, 1, 0, 0], [1, 0, 0, 1, 1]))
print(algebra.product(3, [2, 0, 1, 0, -1]))
print(algebra.multiply([1, 1, -1, 0, 1], [2, -2, 1, 1, 0]))