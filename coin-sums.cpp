int main() {
    int cents;
    cin >> cents;

    int quarters = cents / 25;
    cents %= 25; // subtract quarter's value from total

    int dimes = cents / 10;
    cents %= 10; // subtract dime's value from remaining cents

    int nickles = cents / 5;
    cents %= 5; // subtract nickel's value from remaining cents

    int pennies = cents;

    cout << quarters << endl;
    cout << nickles << endl;
    cout << dimes << endl;
    cout << pennies << endl;

    return 0;
}