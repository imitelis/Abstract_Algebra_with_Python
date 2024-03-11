from structures import Element, Field

# Example of a field operations:
def rational_addition(a, b):
    return (a[0] * b[1] + a[1] * b[0], a[1] * b[1])

def rational_multiplication(a, b):
    return (a[0] * b[0], a[1] * b[1])

# Example usage:
elements = [Element((i, 1)) for i in range(5)] # (a, b) represents a/b
field = Field(elements, rational_addition, rational_multiplication)

print(field.add((1, 2), (1, 3)))
print(field.multiply((1, 2), (1, 3)))