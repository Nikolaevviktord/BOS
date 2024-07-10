# !a
_not = lambda a: int(not a)

# a & b
_and = lambda a, b: int(a and b)

# a | b
_or = lambda a, b: int(a or b)

# a || b
_xor = lambda a, b: int(a ^ b)

# !a | b
_to = lambda a, b: int(_or(_not(a), b))

# a == b
_eq = lambda a, b: int(a == b)

# a != b
_neq = lambda a, b: int(a != b)

# a > b
_more = lambda a, b: int(a > b)

# a < b
_less = lambda a, b: int(a < b)

# a >= b
_me = lambda a, b: _or(_more(a, b), _eq(a, b))

# a <= b
_le = lambda a, b: _or(_less(a, b), _eq(a, b))

print(_me(0, 1))