int main() {
    string str;
    cin >> str;

    bool result = false;
    int count = 0;

    for (char c : str) {
        if (c == '[') {
            count++;
        } else if (c == ']') {
            if (count > 0) {
                count--;
            }
        }

        if (count >= 1 && c == ']') {
            result = true;
            break;
        }
    }

    cout << (result ? "true" : "false");

    return 0;
}