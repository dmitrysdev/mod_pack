def my_filter(iterable, function):

    ret = list(filter(function, iterable))

    return ret

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True

numbers = [10, 15, 21, 33, 42, 55]

mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))

print(mapped_numbers == [23, 33, 45, 69, 87, 113])

s2="hello"

print(sorted(s2) == ['e', 'h', 'l', 'l', 'o'])
print(sorted(s2, reverse=True) == ['o', 'l', 'l', 'h', 'e'])

d1 = {2: 'red', 1: 'green', 3: 'blue'}

print(sorted(d1) == [1, 2, 3])

import math

print(math.pi == 3.141592653589793)
print(math.sqrt(4) == 2)
print(math.pow(5,2) == 25)
print(math.hypot(2, 3) == math.sqrt(13))
