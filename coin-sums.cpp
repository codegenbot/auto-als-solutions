#include <vector>
using namespace std;

vector<int> coinSums(int cents) {
    vector<int> coins(4); // quarters, dimes, nickles, pennies
    while (cents > 0) {
        if (cents >= 25) {
            cents -= 25;
            coins[0]++;
        } else if (cents >= 10) {
            cents -= 10;
            coins[1]++;
        } else if (cents >= 5) {
            cents -= 5;
            coins[2]++;
        } else {
            cents -= 1;
            coins[3]++;
        }
    }
    return coins;
}

int main() {
    int cents;
    cin >> cents;
    vector<int> result = coinSums(cents);
    cout << result[0] << endl;
    cout << result[1] << endl;
    cout << result[2] << endl;
    cout << result[3] << endl;
    return 0;
}