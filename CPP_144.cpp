bool simplify(string x, string n) {
    int a = 0, b = 1, c = 0, d = 1;
    stringstream s(x);
    s >> a >> b;

    stringstream t(n);
    t >> c >> d;

    if (b*d == a*c) return true;
    return false;
}