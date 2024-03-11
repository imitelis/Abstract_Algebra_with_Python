from structures import Element, Group

elements_Z5 = [Element(i) for i in range(5)]
elements_Z4 = [Element(i) for i in range(4)]

# Example of a group operation:
def addition_mod_n(n):
    def inner(a, b):
        return (a + b) % n
    return inner

# Create groups:
group_Z5 = Group(elements_Z5, addition_mod_n(5))
group_Z4 = Group(elements_Z4, addition_mod_n(4))

# Define an isomorphism:
def isomorphism(element_Z5):
    mapping = {0: 0, 1: 1, 2: 3, 3: 2, 4: 0}
    return mapping[element_Z5]

# Apply the isomorphism:
element_Z5 = 2
element_Z4 = isomorphism(element_Z5)

print(element_Z4)
print(element_Z5 == isomorphism(isomorphism(element_Z5)))