double probability(int n, int m) {
    double total = (n + m - 2);
    if(m > n) {
        std::swap(n, m);
    }
    return (double)(m-1)/(n+m-2);
}