#include <iostream>
#include <string>

bool prime_length(string str) {
    int len = str.length();
    bool isPrime = true;

    for (int i = 2; i * i <= len && isPrime; i++) {
        if (len % i == 0)
            isPrime = false;
    }

    return isPrime;
}

int main() {
    assert(prime_length("0") == false);
    std::cout << "The prime length for '0' is: " << (prime_length("0") ? "true" : "false") << std::endl;

    return 0;
}