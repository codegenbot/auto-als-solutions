int fib(int n); // Function declaration

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    cout << "The " << to_string(n) << "-th Fibonacci number is: " << to_string(fib(n)) << endl;
    return 0;
}

int fib(int n) {
    if (n <= 1)
        return n;
    else
        return fib(n-1) + fib(n-2);
}