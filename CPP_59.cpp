#include <iostream>

using namespace std;

int largest_prime_factor(int n) {
    int maxFactor = 1;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            if (i > maxFactor)
                maxFactor = i;
            n /= i;
        }
    }
    return maxFactor;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "The largest prime factor is: " << largest_prime_factor(n) << endl;
    return 0;
}