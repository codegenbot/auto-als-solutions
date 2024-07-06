#include <math.h>

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