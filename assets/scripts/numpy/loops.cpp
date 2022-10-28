#include <iostream>
#include <chrono>
#include <vector>
#include <random>

const unsigned int N = 10'000'000;

int main()
{
    // Готовим генератор случайных чисел в промежутке от -1 до 1
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(-1.0, 1.0);

    // Создаём массивы случайных чисел
    std::vector<double> a(N), b(N), c(N);
    for (int i = 0; i < N; ++i)
    {
        a[i] = dis(gen);
        b[i] = dis(gen);
    }

    // Измеряем время сложения векторов
    auto t1 = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < N; ++i)
        c[i] = a[i] + b[i];

    auto t2 = std::chrono::high_resolution_clock::now();

    auto ms_int = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);
    std::cout << ms_int.count() << " ms";
}