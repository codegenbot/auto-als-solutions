```cpp
#include <iostream>
#include <vector>

using namespace std;

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int skjkasdkd(vector<int> lst) {
    int max_prime = 0;
    for (int num : lst) {
        if (isPrime(num)) {
            if (num > max_prime) {
                max_prime = num;
            }
        }
    }
    int sum_of_digits = 0;
    while (max_prime > 0) {
        sum_of_digits += max_prime % 10;
        max_prime /= 10;
    }
    return sum_of_digits;
}

int main() {
    vector<int> lst;
    cout << "Enter numbers: ";
    int n;
    while ((cin >> n) && (n != -1)) {
        lst.push_back(n);
    }
    int output = skjkasdkd(lst);
    if (!lst.empty()) {
        cout << "The sum of digits for the largest prime in the list is: " << output << endl;
    } else {
        cout << "No numbers entered." << endl;
    }
    return 0;
}