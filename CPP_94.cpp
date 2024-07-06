#include <vector>

int sumOfDigits(int num) {
    int sum = 0;
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int largestPrime(vector<int> lst) {
    for (int i : lst) {
        if (isPrime(i)) {
            return i;
        }
    }
    return -1; 
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

int skjkasdkd(vector<int> lst) {
    int largestPrimeNumber = largestPrime(lst);
    return sumOfDigits(largestPrimeNumber);
}