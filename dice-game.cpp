#include <iostream>

using namespace std;

double diceGame(int n, int m) {
    double p = 0.0;
    for (int i = n + 1; i <= m * 2; i++) {
        p += 1.0 / max(n, m);
    }
    return p;
}

int main() {
    int n, m;
    cin >> n >> m;
    cout << fixed << setprecision(9) << diceGame(n, m) << endl;
    return 0;
}