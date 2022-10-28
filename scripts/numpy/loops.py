from time import perf_counter
from random import uniform


N = 10_000_000

# Создаём списки случайных чисел
# новый синтаксис, список случайных чисел
a = [uniform(-1, 1) for i in range(N)]
b = [uniform(-1, 1) for i in range(N)]
c = [0.0] * N

# Измеряем время сложения этих списков
t1 = perf_counter()

for i in range(N):
    c[i] = a[i] + b[i]

t2 = perf_counter()
print(f"{(t2 - t1) * 1000} ms")  # perf_counter() - время в секундах
