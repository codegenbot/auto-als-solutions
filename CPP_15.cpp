string string_sequence(int n);
int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;
    string result = "";
    for (int i = 1; i <= n; i++) {
        result += to_string(i) + " ";
    }
    cout << result << endl;
    return 0;
}