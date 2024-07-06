#include <bits/stdc++.h>

using namespace std;

int largest_divisor(int n) {
    for (int i = n / 2; i > 0; i--) {
        if (n % i == 0) {
            return i;
        }
    }
    return 1;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Largest divisor is: " << largest_divisor(n) << endl;
    return 0;
}