```cpp
string change_base(int x, int base) {
    string result = "";
    while (x > 0) {
        int remainder = x % base;
        if (remainder < 10)
            result = to_string(remainder) + result;
        else
            result = 'A' + remainder - 10 + result;
        x /= base;
    }
    return result;
}