bool solveBoolean(string s) {
    if(s == "T" || s == "t")
        return true;
    else if(s == "F" || s == "f")
        return false;
    else if(s.find("|") != string::npos) {
        size_t pos = 0;
        int i = 0;
        while (i < s.length()) {
            if (s[i] == '|') {
                string a = s.substr(pos, i - pos);
                string b = s.substr(i + 1);
                return solveBoolean(a) || solveBoolean(b);
            }
            i++;
        }
    } else if(s.find("&") != string::npos) {
        size_t pos = 0;
        int i = 0;
        while (i < s.length()) {
            if (s[i] == '&') {
                string a = s.substr(pos, i - pos);
                string b = s.substr(i + 1);
                return solveBoolean(a) && solveBoolean(b);
            }
            i++;
        }
    } else {
        cout << "Invalid input. Only T/F/&( )| are allowed.";
    }
}