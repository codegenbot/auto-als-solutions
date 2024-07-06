string string_sequence(int n);
int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;
    cout << "The sequence is: " << string_sequence(n) << endl;
    return 0;
}

string string_sequence(int n) {
    string result = "";
    for (int i = 1; i <= n; i++) {
        result += to_string(i) + " ";
    }
    return result;
}