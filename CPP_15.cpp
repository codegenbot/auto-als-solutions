```cpp
string string_sequence(int n);
int main() {
    int n;
    cin >> n;
    cout << string_sequence(n) << endl;
}

string string_sequence(int n) {
    string result = "";
    for (int i = 0; i <= n; i++) {
        result += to_string(i) + " ";
    }
    return result;
}