"""Lambda, map, and filter."""
values = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n * n, values))
evens = list(filter(lambda n: n % 2 == 0, values))
print(squares, evens)
