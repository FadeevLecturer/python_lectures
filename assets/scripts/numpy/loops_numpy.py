from time import perf_counter
from numpy.random import uniform


N = 10_000_000

# Создаём массивы случайных чисел
a = uniform(-1, -1, size=N)
b = uniform(-1, -1, size=N)


# Измеряем время сложения этих списков
t1 = perf_counter()
c = a + b
t2 = perf_counter()
print(f"{(t2 - t1) * 1000} ms")  # perf_counter() - время в секундах
