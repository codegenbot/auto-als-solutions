#include <iostream>
#include <vector>

int solveProblem(std::vector<int> lst) {
    int maxPrime = 0;
    for (int num : lst) {
        if (isPrime(num)) {
            if (num > maxPrime) {
                maxPrime = num;
            }
        }
    }
    int sumOfDigits = 0;
    while (maxPrime > 0) {
        sumOfDigits += maxPrime % 10;
        maxPrime /= 10;
    }
    return sumOfDigits;
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

int main() {
    assert(solveProblem({127, 97, 8192}) == 10);
    int n;
    std::cout << "Enter the number of integers: ";
    std::cin >> n;
    std::vector<int> lst(n);
    for (int i = 0; i < n; i++) {
        std::cout << "Enter integer " << i+1 << ": ";
        std::cin >> lst[i];
    }
    int result = solveProblem(lst);
    std::cout << "Sum of digits of the maximum prime number is: " << result;
    return 0;
}