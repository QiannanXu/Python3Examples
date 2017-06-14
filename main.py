from src import humansize

print(humansize.approximate_size(1000000000000, False))
print(humansize.approximate_size(1000000000000))
print(humansize.approximate_size.__doc__)