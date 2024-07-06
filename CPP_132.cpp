int main() {
    string str;
    cin >> str;

    bool is_nested = false;
    int count_open = 0;
    for (char c : str) {
        if (c == '[') {
            count_open++;
        } else if (c == ']') {
            if (count_open > 1) {
                is_nested = true;
                break;
            }
            count_open--;
        }
    }

    cout << (is_nested ? "true" : "false") << endl;

    return 0;
}