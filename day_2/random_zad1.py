import random

# operacje na liczbach losowych

#  """Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # od 1 do 100 int

print(random.randrange(1, 100))  # od 1 do 99 int
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # 0.8239814245049077 float od 0 do 0.999999
print(random.random() * 8)  # 6.576811415721201 float od 0 do 7.999999
