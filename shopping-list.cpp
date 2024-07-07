#include <vector>
using namespace std;

double shoppingList(double price[], int n, double discount[]) {
    double total = 0;
    for (int i = 0; i < n; i++) {
        double p = price[i];
        double d = p * discount[i] / 100;
        total += p - d;
    }
    return total;
}

int main() {
    int N;
    cin >> N;
    vector<double> prices(N);
    for (auto& p : prices) {
        cin >> p;
    }
    vector<double> discounts(N);
    for (auto& d : discounts) {
        cin >> d;
    }
    cout << fixed << setprecision(1) << shoppingList(&prices[0], N, &discounts[0]) << endl;
    return 0;
}