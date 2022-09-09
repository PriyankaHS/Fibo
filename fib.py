def fib():
    a = 0
    b = 1
    while True:
        yield a
        c = b + a
        a=b
        b=c
f = fib()

for _ in range(1,10):
    print(next(f))
    