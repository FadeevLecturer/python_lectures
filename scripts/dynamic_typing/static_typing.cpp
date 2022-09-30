#include<iostream>

#define FIRSTBYTE   1
#define SECONDBYTE  256
#define THIRDBYTE   256*256
#define FOURTHBYTE  256*256*256


int main(){
    // 1
    int a = 65*FIRSTBYTE + 66*SECONDBYTE + 67*THIRDBYTE + 68*FOURTHBYTE;
    std::cout << a << std::endl;                // 1145258561

    // 2
    char *b = reinterpret_cast<char*>(&a);
    // 3
    for(size_t i=0; i<4; ++i)
        std::cout << b[i];                      // ABCD
    std::cout << std::endl;

    // 4
    a = 'A';
    std::cout << a;                             // 65

    return 0;
}