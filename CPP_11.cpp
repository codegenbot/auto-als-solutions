```cpp
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

int main() {
    assert (string_xor("0101", "0000") == "0101");
    return 0;
}