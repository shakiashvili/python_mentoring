
# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries
from typing import Callable, Union


def merge_elems(*elems: [int, list, str]) -> Union[int, str]:
    for element in elems:
        if isinstance(element, (list, tuple, set)):
            for i in merge_elems(*element):
                yield i
        else:
            element = [element]
            yield from element

# example input


a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')

# # output: 1 2 3 6 z h a b a 1 2 3 4

# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception


def map_like(fun: Callable[Union[str, int, list], [str, int]], 
             *elems: Union[str, list, int]) -> Union[int, str]: 
    try:
        for elem in elems:
            if iter(elem):
                yield fun(elem)
    except TypeError as e:
        yield f"{elem}: {e}"

# example input


a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun = lambda x: x[0]


for _ in map_like(fun, a, b, c, d):
    print(_)

# output:
# 1
# 6: 'int' object is not subscriptable
# z
# True: 'bool' object is not subscriptable
