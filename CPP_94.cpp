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
    vector<int> input;
    cout << "Enter the numbers (space separated): ";
    string str;
    getline(cin, str);
    size_t pos = 0;
    while ((pos = str.find(" ")) != string::npos) {
        input.push_back(stoi(str.substr(0, pos)));
        str.erase(0, pos + 1);
    }
    if (!str.empty()) {
        input.push_back(stoi(str));
    }

    int output = skjkasdkd(input);

    cout << "The sum of digits is: " << output << endl;

    return 0;
}