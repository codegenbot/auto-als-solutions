```cpp
int x_or_y(int n, int x, int y) {
    if (n == 2) return x;
    bool isPrime = true;
    if (n <= 1) {
        return y;
    }
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }
    return isPrime ? x : y;
}