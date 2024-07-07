Here is the completed code:

double diceGame(int n, int m) {
    if (n < m) return 0;
    double total = (double)n * m;
    int count = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j < m; j++) {
            if (i > j) count++;
        }
    }
    return (double)count / total;
}