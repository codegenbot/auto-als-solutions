```
#include <iostream>

using namespace std;

int fibfib(int n) {
    if (n <= 1)
        return 0;
    else if (n == 2)
        return 1;
    else {
        int a = 0, b = 0, c = 1;
        for (int i = 3; i <= n; i++) {
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp % 2 == 0 ? c : c - ((c/2)*(c/2));
        }
        return c;
    }
}

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    cout << "FibFib number at position " << n << " is " << fibfib(n) << endl;
    return 0;
}