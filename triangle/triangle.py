def judge(a, b, c):
    if not(a < b + c and b < a + c and c < a + b):
        raise NonTriangleException()

    if a == b == c:
        return 1
    elif a == b:
        return 2
    return 3

class NonTriangleException(Exception):
    pass