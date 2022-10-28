from typing import Iterator
from math import sqrt
import argparse

from memory_profiler import profile as memory_profiler
from timed import timed as time_profiler


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", type=int, default=1_000_000, help="Верхний предел суммирования")
    parser.add_argument("--memory", action="store_true", help="Профилировать по памяти")
    parser.add_argument("--time", action="store_true", help="Профилировать по времени")
    return parser.parse_args()


def list_of_terms(N: int) -> list[float]:
    return [1./(n * n) for n in range(1, N)]


def generator_of_terms(N: int) -> Iterator[float]:
    for n in range(1, N):
        yield 1./(n * n)


def map_of_terms(N: int) -> Iterator[float]:
    return map(lambda n: 1./(n*n), range(1, N))


def list_implementation(N: int) -> float:
    terms = list_of_terms(N)
    s = sum(terms)
    return sqrt(6. * s)


def generator_implementation(N: int) -> float:
    terms = generator_of_terms(N)
    s = sum(terms)
    return sqrt(6. * s)


def map_implementation(N: int) -> float:
    terms = map_of_terms(N)
    s = sum(terms)
    return sqrt(6. * s)


def main():
    args = parse_args()

    functions = [list_implementation, generator_implementation, map_implementation]
    if args.memory:
        functions = [memory_profiler(f) for f in functions]
    if args.time:
        functions = [time_profiler(f) for f in functions]

    for f in functions:
        print(f"{f.__name__:30} {f(args.N)}")


if __name__ == "__main__":
    main()