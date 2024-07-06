```
#include <vector>
#include <iostream>

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
        } else if (i > maxPrime) {
            maxPrime = i;
        }
    }
    return sumOfDigits(maxPrime);
}

int main() {
    vector<int> lst;
    int n;
    std::cin >> n;
    while (n--) {
        cin >> n;
        lst.push_back(n);
    }
    std::cout << largestPrime(lst) << endl;
    return 0;
}