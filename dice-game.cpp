#include <iostream>
using namespace std;

double getProbability(int n, int m) {
    if(n == 1 || m == 1) return 0.0;
    return (n - 1.0) / (n + m - 2.0);
}

int main() {
    int n, m;
    cin >> n >> m;
    cout << fixed << setprecision(4) << getProbability(n, m) << endl;
    return 0;
}