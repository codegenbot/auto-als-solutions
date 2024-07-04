#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> digits(16);
    for (int i = 0; i < 16; ++i) {
        cin >> digits[i];
    }

    int sum = 0;
    for (int i = 0; i < 16; ++i) {
        int value = digits[i];
        if (i % 2 == 0) {
            value *= 2;
            if (value > 9) {
                value -= 9;
            }
        }
        sum += value;
    }

    cout << sum << endl;
    return 0;
}