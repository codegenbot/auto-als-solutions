int fib(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    if (fib(30) > 268934816) {
        std::cout << "Error: Fibonacci number exceeded maximum limit!" << std::endl;
    } else {
        int n;
        std::cout << "Enter a positive integer: ";
        std::cin >> n;
        std::cout << "Fibonacci of " << n << ": " << fib(n) << std::endl;
    }
    return 0;
}