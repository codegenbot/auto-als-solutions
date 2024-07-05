string change_base(int x, int base) {
    string res("");
    while (x > 0) {
        int rem = x % base;
        char c = rem < 10 ? '0' + rem : rem > 9 ? 'A' + rem - 10 : '-';
        res += c; 
        x /= base;
    }
    return res;
}