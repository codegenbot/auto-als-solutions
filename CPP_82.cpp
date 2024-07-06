```cpp
#include <iostream>
#include <string>

std::string str;

bool prime_length(const std::string& s) {
    int len = s.length();
    bool is_prime = true;
    if(len <= 1)
        return false;
    for(int i=2; i*i<=len; i++){
        if(len%i==0)
            is_prime = false;
    }
    return is_prime;
}

int main() {
    std::cout << "Enter a string: ";
    std::cin >> str;
    std::cout << (prime_length(str) ? "true" : "false") << std::endl;
    return 0;
}