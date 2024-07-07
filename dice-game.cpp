double probability(int n, int m) {
    double total = (n + m - 2);
    if(m > n) return 0;
    return (double)(m-1)/total;
}