```cpp
#include <iostream>
using namespace std;

int main() {
    int cents;
    cin >> cents;
    
    int pennies = cents;
    int quarters = 0;

    while(pennies >= 25) {
        quarters++;
        pennies -= 25;
    }

    int nickles = pennies / 5;
    pennies %= 5;

    int dimes = pennies / 10;
    pennies %= 10;

    cout << quarters << endl;
    cout << nickles << endl;
    cout << dimes << endl;
    cout << pennies << endl;

    return 0;
}