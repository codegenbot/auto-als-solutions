#include <iostream>

int fibfib(int n) {
    if (n <= 1)
        return 0;
    else if (n == 2)
        return 1;
    else {
        int a = 0, b = 1, c = 1;
        for (int i = 3; i <= n; i++) {
            int temp = a + b + c;
            a = b;
            b = c;
            c = temp;
        }
        return c;
    }
}

int main() {
    int n;
    std::cout << "Enter the value of n: ";
    std::cin >> n;
    std::cout << "FibFib number at position " << n << " is " << fibfib(n) << std::endl;
    return 0;
}