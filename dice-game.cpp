#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int count = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (i > j) {
                count++;
            }
        }
    }

    double total = n * m;
    double probability = static_cast<double>(count) / total;
    cout << probability << endl;

    return 0;
}