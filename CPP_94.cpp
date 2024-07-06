#include <vector>

int sumOfDigits(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int largestPrime(vector<int> lst) {
    int max_prime = -1;
    for (int i : lst) {
        if (isPrime(i)) {
            if (i > max_prime)
                max_prime = i;
        }
    }
    return max_prime;
}

int skjkasdkd(vector<int> lst) {
    int largestPrimeNumber = largestPrime(lst);
    return sumOfDigits(largestPrimeNumber);
}