string squareDigits(int n) {
    string result = "";
    string numStr = to_string(n);
    for (char c : numStr) {
        int digit = c - '0';
        result += to_string(digit * digit);
    }
    return result;
}

int main() {
    int n;
    cin >> n;
    cout << squareDigits(n) << endl;
    return 0;
}