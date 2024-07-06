```cpp
#include <iostream>
#include <string>

bool prime_length(const std::string& str) {
    int len = str.length();
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
    std::cout << (prime_length("0") ? "true" : "false") << std::endl;
}