#include <iostream>
using namespace std;

double solve(int n, int m) {
    double sum = 0.0;
    for (int i = n + 1; i <= m; i++) {
        sum += 1.0 / (n * 1.0);
    }
    return sum;
}

int main() {
    int n, m;
    cin >> n >> m;
    double result = solve(n, m);
    cout << fixed << setprecision(1) << result << endl;
    return 0;
}