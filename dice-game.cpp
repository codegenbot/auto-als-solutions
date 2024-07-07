Here is the solution:

double diceGame(int n, int m) {
    if (n < m) swap(n, m);
    return 1.0 * (m + 1) / (double)(n);
}