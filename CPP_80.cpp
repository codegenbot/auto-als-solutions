bool is_happy(string s) {
    int len = s.length();
    if(len < 3) return false;
    for(int i = 0; i <= len-3; i++) {
        bool unique = true;
        for(int j = i+1; j <= i+3; j++) {
            if(s[j-1] == s[j]) {
                unique = false;
                break;
            }
        }
        if(unique) return true;
    }
    return false;
}