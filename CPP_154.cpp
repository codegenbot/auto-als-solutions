bool cycpattern_check(string a, string b) {
    for(int i = 0; i < a.length(); i++) {
        string s = a.substr(i);
        if(s.length() >= b.length()) {
            int j = 0;
            while(j < b.length()) {
                if(s[j] != b[j]) break;
                j++;
            }
            if(j == b.length()) return true;
        }
    }
    return false;
}