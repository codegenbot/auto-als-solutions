bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty()) return false;
    string lastChar = txt.substr(txt.length() - 1);
    return isalpha(lastChar[0]) && !isalnum(lastChar[0]);
}

int main() {
    string input;
    cout << "Enter a string: ";
    cin >> input;
    
    if (check_if_last_char_is_a_letter(input)) {
        cout << "The last character of the input string is a letter." << endl;
    } else {
        cout << "The last character of the input string is not a letter." << endl;
    }
    
    return 0;
}