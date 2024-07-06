int max_unique = 0;
string res;
for (const string& s : words) {
    int count = 0;
    set<char> unique_chars(s.begin(), s.end());
    if ((int)unique_chars.size() > max_unique) {
        max_unique = (int)unique_chars.size();
        res = s;
    }
}
return res;