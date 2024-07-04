string spinWords(const string &str) {
    istringstream iss(str);
    string word, result;
    bool first = true;
    while (iss >> word) {
        if (word.length() >= 5) {
            reverse(word.begin(), word.end());
        }
        if (!first) result += " ";
        result += word;
        first = false;
    }
    return result;
}

int main() {
    string input;
    getline(cin, input);
    cout << spinWords(input) << endl;
    return 0;
}