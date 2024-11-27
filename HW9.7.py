def is_prime(func):
    def wrapper(*args):
        p = False
        original = func(*args)
        if original != 0:
            for i in range(2, original):
                if original % i != 0:
                    p = True
                else:
                    p = False
                    break
        if p:
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
