int main() {
    int n;
    cin >> n;
    vector<int> digits(n);
    for (int i = 0; i < n; ++i) {
        cin >> digits[i];
    }

    int sum = 0;
    for (int i = 0; i < n; ++i) {
        int value = digits[i];
        if (i % 2 == 1) {
            value *= 2;
            if (value > 9) {
                value -= 9;
            }
        }
        sum += value;
    }

    cout << sum << endl;
    return 0;
}