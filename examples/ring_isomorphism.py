from structures import Element, Ring

elements_Z5 = [Element(i) for i in range(5)]
elements_Z4 = [Element(i) for i in range(4)]

# Example of a ring operations:
def addition_mod_n(n):
    def inner(a, b):
        return (a + b) % n
    return inner

def multiplication_mod_n(n):
    def inner(a, b):
        return (a * b) % n
    return inner

# Create rings:
ring_Z5 = Ring(elements_Z5, addition_mod_n(5), multiplication_mod_n(5))
ring_Z4 = Ring(elements_Z4, addition_mod_n(4), multiplication_mod_n(5))

# Define an isomorphism:
def isomorphism(element_Z5):
    mapping_add = {0: 0, 1: 1, 2: 3, 3: 2, 4: 0}
    mapping_multiply = {0: 0, 1: 1, 2: 3, 3: 2, 4: 0}
    return mapping_add[element_Z5], mapping_multiply[element_Z5]

# Apply the isomorphism:
element_Z5 = 2
element_Z4_add, element_Z4_multiply = isomorphism(element_Z5)

print(element_Z4_add, element_Z4_multiply)
print(element_Z5 == isomorphism(isomorphism(element_Z5)[0])[0])
print(element_Z5 == isomorphism(isomorphism(element_Z5)[1])[1])