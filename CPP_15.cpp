string string_sequence(int n);
int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Sequence of numbers from 0 to " << n << ": " << string_sequence(n) << endl;
    return 0;
}

string string_sequence(int n) {
    string result = "";
    for (int i = 0; i <= n; i++) {
        result += to_string(i) + " ";
    }
    return result;
}