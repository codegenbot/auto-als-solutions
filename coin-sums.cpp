#include <iostream>
using namespace std;

int main() {
    int cents;
    cin >> cents;

    vector<int> coins = {25, 10, 5, 1};
    vector<int> coinCounts(4, 0);

    for (int i = 3; i >= 0; i--) {
        while (cents >= coins[i]) {
            int count = cents / coins[i];
            cents -= count * coins[i];
            coinCounts[i] = count;
        }
    }

    cout << coinCounts[3] << endl;
    cout << coinCounts[2] << endl;
    cout << coinCounts[1] << endl;
    cout << coinCounts[0] << endl;

    return 0;
}