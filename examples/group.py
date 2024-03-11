from structures import Element, Group

# Example of a group operation:
def addition_mod_n(n):
    def inner(a, b):
        return (a + b) % n
    return inner

# Example usage:
elements = [Element(i) for i in range(5)]
group = Group(elements, addition_mod_n(2))

print(group.apply(2, 3))