Here is the solution:

double diceGame(int n, int m) {
    double total = (long long)n * m;
    return (n - 1) / (double)total;
}