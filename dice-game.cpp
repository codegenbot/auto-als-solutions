```cpp
double probability(int n, int m) {
    double total = (n + m - 1);
    if(m == 1) return 1;
    return (double)(m-1)/total;
}