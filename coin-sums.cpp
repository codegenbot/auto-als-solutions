#include <iostream>

using namespace std;

int main() {
    int cents;
    cin >> cents;

    int quarters = cents / 25;
    cents %= 25;

    int dimes = quarters * 2 + (cents / 10) % 4;
    cents %= 10;

    int nickles = dimes * 2 + (cents / 5) % 20 / 10;
    cents %= 5;

    int pennies = cents;

    cout << quarters << endl;
    cout << nickles << endl;
    cout << dimes << endl;
    cout << pennies << endl;

    return 0;
}