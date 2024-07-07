#include <iostream>
using namespace std;

int main() {
    int cents;
    cin >> cents;
    
    int quarters = cents / 25;
    int remainder = cents % 25;
    
    int dimes = remainder / 10;
    remainder = remainder % 10;
    
    int nickles = remainder / 5;
    remainder = remainder % 5;
    
    int pennies = remainder;
    
    cout << quarters << endl;
    cout << dimes << endl;
    cout << nickles << endl;
    cout << pennies << endl;

    return 0;
}