from structures import Element, NormedSpace

# Example of a normed space operations:
def vector_addition(a, b):
    return [x + y for x, y in zip(a, b)]

def scalar_product(r, a):
    return [r * x for x in a]

def vector_norm(a):
    return sum(x**2 for x in a)**0.5

# Example usage:
basis = [Element([1, 0, 0]), Element([0, 1, 0]), Element([0, 0, 1])]
normed_space = NormedSpace(basis, vector_addition, scalar_product, vector_norm)

print(normed_space.add([1, 0, 0], [1, 0, 0]))
print(normed_space.product(3, [2, 0, 1]))
print(normed_space.norm([1, 2, -1]))