#include<iostream>
#include<string>

int f(int x){
    return x + 1;
}

int main(){
	std::string s = "abc";
	std::cout << f(s);
}