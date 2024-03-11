from structures import Element, VectorSpace

# Example of a vector space operations:
def vector_addition(a, b):
    return [x + y for x, y in zip(a, b)]

def scalar_product(r, a):
    return [r * x for x in a]

# Example usage:
basis = [Element([1, 0, 0]), Element([0, 1, 0]), Element([0, 0, 1])]
vector_space = VectorSpace(basis, vector_addition, scalar_product)

print(vector_space.add([1, 0, 0], [1, 0, 0]))
print(vector_space.product(3, [2, 0, 1]))