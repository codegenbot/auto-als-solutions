int main() {
    string cipher1, cipher2, message;
    cin >> cipher1 >> cipher2 >> message;

    map<char, char> cipherMap;
    for (size_t i = 0; i < cipher1.size(); ++i) {
        cipherMap[cipher1[i]] = cipher2[i];
    }

    string decipheredMessage;
    for (char ch : message) {
        decipheredMessage += cipherMap[ch];
    }

    cout << decipheredMessage << endl;
    return 0;
}