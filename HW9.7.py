def is_prime(func):
    def wrapper(*args):
        original = func(*args)
        if (int(original) % 2 != 0 and
                int(original) % 3 != 0 and
                int(original) % 4 != 0):
            print('Простое')
        else:
            print('Сложное')
        return original
    return wrapper

@is_prime
def sum_three(*args):
    y = 0
    for i in args:
        y += i
    return y

result = sum_three(2, 3, 6)
print(result)
