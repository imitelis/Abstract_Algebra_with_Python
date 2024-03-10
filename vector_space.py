from element import Element

# Example of a vector space class:
class VectorSpace:
    def __init__(self, elements, vector_addition, scalar_product, dot_product, cross_product):
        self.elements = elements
        self.vector_addition = vector_addition
        self.scalar_product = scalar_product
        self.dot_product = dot_product
        self.cross_product = cross_product

    def vector_addition(self, a, b):
        return self.vector_addition(a, b)
    
    def scalar_product(self, r, a):
        return self.scalar_product(r, a)

    def dot_product(self, a, b):
        return self.dot_product(a, b)
    
    def cross_product(self, a, b):
        return self.cross_product(a, b)

    def zero(self):
        return None

    def identity(self):
        return None

    def inverse(self):
        return None

# Example of a vector field operations:
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
basis = [Element([1, 0, 0]), Element([0, 1, 0]), Element([0, 0, 1])]
vector_space = VectorSpace(basis, vector_addition, scalar_product, dot_product, cross_product)

print(vector_space.vector_addition([1, 0, 0], [1, 0, 0]))
print(vector_space.scalar_product(3, [2, 0, 1]))
print(vector_space.dot_product([3, 9, 0], [2, 0, 1]))
print(vector_space.cross_product([-1, 0, 1], [0, 0, -1]))