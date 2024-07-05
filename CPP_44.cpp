string change_base(int x, int base) {
    if (x < base) {
        return to_string(x);
    }
    string res = "";
    while (x > 0) {
        res = to_string(x % base) + res;
        x /= base;
    }
    return res;
}