int main() {
    int cents;
    cin >> cents;
    
    // Calculate quarters
    int quarters = cents / 25;
    cents %= 25;

    while(cents >= 25) {
        quarters++;
        cents -= 25;
    }

    // Calculate dimes, nickles, and pennies after quarters are accounted for
    int dimes = 0;
    int remainingCents = cents;
    
    while(remainingCents >= 10) {
        dimes++;
        remainingCents -= 10;
    }
    
    int nickles = remainingCents / 5;
    remainingCents %= 5;

    // Calculate pennies
    int pennies = remainingCents;
    
    cout << quarters << endl;
    cout << nickles << endl;
    cout << dimes << endl;
    cout << pennies << endl;

    return 0;
}