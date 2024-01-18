def contador(max_value):
    count = 0
    while count <= max_value:
        yield count
        count += 1


gen = contador(5)

item = next(gen)
print(f"Opa, item {item}")

item = next(gen)
print(f"Opa, item {item}")

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

