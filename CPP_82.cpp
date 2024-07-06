#include <iostream>
#include <string>

bool prime_length(const std::string& str) {
    int len = str.length();
    bool isPrime = true;

    for (int i = 2; i * i <= len && isPrime; i++) {
        if (len % i == 0)
            isPrime = false;
    }

    return isPrime;
}

int main() {
    std::string str;
    std::cout << "Enter a string: ";
    std::getline(std::cin, str);
    
    if(prime_length(str)) {
        std::cout << "The length of the string is prime." << std::endl;
    } else {
        std::cout << "The length of the string is not prime." << std::endl;
    }
    
    return 0;
}