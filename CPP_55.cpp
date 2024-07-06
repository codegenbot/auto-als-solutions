int main {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    cout << "The " << to_string(n) << "-th Fibonacci number is: " << to_string(fib(n)) << endl;
    return 0;
}