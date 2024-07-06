int main() {
    string a = "0101";
    string b = "0000";
    string result = string_xor(a, b);
    // You can use the result here or print it out
    return 0;
}
string string_xor(string a, string b) {
    string result = "";
    for (int i = 0; i < a.size(); i++) {
        int val1 = a[i] - '0';
        int val2 = b[i] - '0';
        int xorVal = val1 ^ val2;
        char c = xorVal + '0';
        result += c;
    }
    return result;
}