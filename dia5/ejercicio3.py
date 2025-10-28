def ceros_repetidos(*args):
    for i in range(1, len(args)):
        if args[i] == 0 and args[i-1] == 0:
            return True
    return False

print(ceros_repetidos(5, 6, 1, 0, 0, 9, 3, 5))
print(ceros_repetidos(6, 0, 5, 1, 0, 3, 0, 1))