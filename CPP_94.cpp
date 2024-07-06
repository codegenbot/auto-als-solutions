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
    cout << "Enter numbers (enter 'stop' to stop input): ";
    string s;
    while (true) {
        cin >> s;
        if (s == "stop") break;
        int num = stoi(s);
        lst.push_back(num);
    }
    cout << "The sum of the digits of the maximum prime number is: " << skjkasdkd(lst) << endl;
    return 0;
}