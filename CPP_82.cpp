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

int mainHelper() {
    std::string str;
    std::cout << "Enter a string: ";
    std::cin >> str;
    std::cout << (prime_length(str) ? "true" : "false") << std::endl;
    return 0;
}