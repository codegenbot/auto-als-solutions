bool simplify(string x, string n) {
    int a = 1, b = 1, c = 1, d = 1;
    istringstream XX(x);
    XX >> a >> c;
    istringstream YY(n);
    YY >> b >> d;

    return (a*d == b*c);
}