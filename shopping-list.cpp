#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int n;
    if (!(cin >> n)) return 1;

    vector<double> prices(n), discounts(n);
    for (int i = 0; i < n; ++i) {
        if (!(cin >> prices[i])) return 1;
    }

    for (int i = 0; i < n; ++i) {
        if (!(cin >> discounts[i]) || discounts[i] < 0 || discounts[i] > 100) return 1;
    }

    double total = 0.0;
    for (int i = 0; i < n; ++i) {
        total += prices[i] * (1 - discounts[i] / 100.0);
    }

    cout << fixed << setprecision(2) << total << endl;
    return 0;
}