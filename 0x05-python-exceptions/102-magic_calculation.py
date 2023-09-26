import dis

"""
Write the Python function def magic_calculation(a, b):
that does exactly the same as the following Python bytecode:
"""


def magic_calculation(a, b):
    result = 0

    if a > b:
        result = a + b
    else:
        result = a - b

    return result


dis.dis(magic_calculation)
