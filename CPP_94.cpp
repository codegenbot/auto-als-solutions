#include <vector>
#include <initializer_list>

int sumOfDigits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int largestPrime(vector<int> lst) {
    int maxPrime = -1;
    for (int i = 2; i <= 100000; i++) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            for (int num : lst) {
                if (num > i) {
                    return sumOfDigits(i);
                }
            }
        } else {
            maxPrime = i;
        }
    }
    return maxPrime;
}

int skjkasdkd(vector<int> lst) {
    int maxPrime = largestPrime(lst);
    if (maxPrime == -1) {
        return 0;
    } else {
        return sumOfDigits(maxPrime);
    }
}