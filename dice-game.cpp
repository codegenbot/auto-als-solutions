#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    double totalOutcomes = static_cast<double>(n) * m;
    double favorableOutcomes = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (i > j) {
                favorableOutcomes++;
            }
        }
    }

    double probability = favorableOutcomes / totalOutcomes;
    cout << fixed << setprecision(8) << probability << endl;

    return 0;
}