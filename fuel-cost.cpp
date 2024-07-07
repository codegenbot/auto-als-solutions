int getFuel(int n) {
    return (n / 3) - 2;
}

long long totalFuel(vector<int> numbers) {
    long long sum = 0;
    for (int i : numbers) {
        sum += getFuel(i);
    }
    return sum;
}

int main() {
    int numInputs;
    cin >> numInputs;
    vector<int> inputs(numInputs);
    for (int& input : inputs) {
        cin >> input;
    }
    cout << totalFuel(inputs) << endl;
    return 0;
}