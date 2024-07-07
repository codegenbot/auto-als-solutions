```cpp
double probability(int n, int m) {
    double total = (n - 1)*(m - 1);
    return (double)(m-1)/total;
}