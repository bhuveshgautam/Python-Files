def powersOfTwo():
    i = 0
    def iter(i = 0):
        yield 2 ** i
        i += 1
        iter(i + 1)
    return iter
