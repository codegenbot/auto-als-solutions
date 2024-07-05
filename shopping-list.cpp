#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<double> prices(n);
    for (int i = 0; i < n; ++i) {
        cin >> prices[i];
    }

    vector<double> discounts(n);
    for (int i = 0; i < n; ++i) {
        cin >> discounts[i];
    }

    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += static_cast<long long>(prices[i] * 100) * (100 - static_cast<long long>(discounts[i]));
    }

    cout << fixed << setprecision(2) << total / 10000.0 << endl;
    return 0;
}