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
    vector<int> numbers;
    cout << "Enter a sequence of space separated integers: ";
    string input;
    getline(cin, input);
    for (string::iterator it = input.begin(); it != input.end(); ++it) {
        if (*it == ' ') {
            continue;
        }
        int num = 0;
        for (; it != input.end() && isdigit(*it); ++it) {
            num = num * 10 + (*it - '0');
        }
        numbers.push_back(num);
    }

    cout << "The sum of the digits of the largest prime number in your sequence is: " << skjkasdkd(numbers) << endl;

    return 0;
}