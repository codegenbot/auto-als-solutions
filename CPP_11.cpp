Here is the completed code:

```cpp
string string_xor(string a, string b) {
    string result = "";
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == '1' && b[i] == '1') continue;
        if (a[i] == '0' && b[i] == '0') continue;
        result += (a[i] ^ b[i]) + '';
    }
    return result;
}