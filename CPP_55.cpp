int fib(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    if (b > 500000) {
        std::cout << "Fibonacci number too large. It is greater than 500,000." << std::endl;
    } else {
        return b;
    }
}

int main() {
    assert(fib(12) == 144);
    // Add more test cases or your code logic here
    return 0;
}