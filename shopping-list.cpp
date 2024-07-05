#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<double> prices(n);
    for (int i = 0; i < n; ++i) {
        cin >> fixed >> setprecision(2) >> prices[i];
    }

    vector<double> discounts(n);
    for (int i = 0; i < n; ++i) {
        cin >> fixed >> setprecision(2) >> discounts[i];
    }

    double total = 0.0;
    for (int i = 0; i < n; ++i) {
        total += prices[i] * (1 - discounts[i] / 100.0);
    }

    cout << fixed << setprecision(2) << total << endl;
    return 0;
}