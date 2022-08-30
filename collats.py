def steps(n):
    x = 0
    while n != 1:
        if n < 1:
            raise ValueError("Only positive integers are allowed")
        elif n % 2 == 0:
            n = n / 2
            x += 1
        else:
            n = (n * 3) + 1
            x += 1
    return x


print(steps(12))
