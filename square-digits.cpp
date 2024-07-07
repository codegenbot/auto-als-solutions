string squareDigits(string input) {
    string output = "";
    for (char c : input) {
        int digit = c - '0';
        long long squared = (long long)digit * digit;
        char squaredChar = '0' + (squared % 10);
        output += squaredChar;
    }
    return output;
}