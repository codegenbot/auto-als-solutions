double probability(int n, int m) {
    double total = 1.0 * (n + m - 2);
    return (total > 0) ? (m-1)/total : 0;
}