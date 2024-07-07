int main() {
    int cents;
    cin >> cents;

    // Number of each type of coin needed
    int pennies = cents / 1;
    int nickles = (cents % 100) / 25;
    int dimes = (cents % 25) / 10;
    int quarters = cents / 25;

    cout << pennies << endl;
    cout << nickles << endl;
    cout << dimes << endl;
    cout << quarters << endl;

    return 0;
}