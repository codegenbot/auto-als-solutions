bool check(string s) {
    int count = 0;
    for (char c : s) {
        if (c == '(')
            count++;
        else if (c == ')')
            count--;
        if (count < 0)
            return false;
    }
    return count == 0;
}

string match_parens(vector<string> lst) {
    string a = lst[0], b = lst[1];
    int openA = 0, closeB = 0;
    for (char c : a) {
        if (c == '(')
            openA++;
        else
            break;
    }
    for (int i = b.size() - 1; i >= 0; i--) {
        if (b[i] == ')')
            closeB++;
        else
            break;
    }
    if ((openA + closeB) % 2 == 0 && check(a + b))
        return "Yes";
    else
        return "No";
}