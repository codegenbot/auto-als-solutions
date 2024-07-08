#include <iostream>
using namespace std;

int main() {
    int cents;
    cin >> cents;

    int quarters = cents / 25;
    cents %= 25;

    int dimes = cents / 10;
    if (dimes > 0) {
        cout << dimes << endl;  
        cents %= 10;
    } else {
        dimes = 0;
    }

    int nickles = cents / 5;
    if (nickles > 0) {
        cout << nickles << endl;   
        cents %= 5;
    } else {
        nickles = 0;
    }

    cout << cents << endl;   

    return 0;
}