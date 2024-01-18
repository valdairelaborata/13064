
my_list = [1, 2, 3, 4, 5, 6]
my_iterator = iter(my_list)

try:
    while True:
        element = next(my_iterator)
        print(element)

except StopIteration:
    pass

print("Fim!")