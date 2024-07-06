#include <cmath>
using namespace std;

int main() {
    long long n;
    cout << "Enter a number: ";
    cin >> n;
    
    if (is_prime(n)) {
        cout << n << " is a prime number." << endl;
    } else {
        cout << n << " is not a prime number." << endl;
    }
    return 0;
}

bool is_prime(long long n) {
    if (n <= 1)
        return false;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}