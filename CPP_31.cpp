#include <math.h>

using namespace std;

int main() {
    long long n;
    cout << "Enter a number: ";
    cin >> n;
    
    if (is_prime(n)) {
        cout << "The number is prime." << endl;
    } else {
        cout << "The number is not prime." << endl;
    }
    
    return 0;
}