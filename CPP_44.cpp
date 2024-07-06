string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int remainder = x % base;
        if (remainder < 10)
            res.insert(0, to_string(remainder));
        else
            res.insert(0, "A");
        x /= base;
    }
    return res;
}