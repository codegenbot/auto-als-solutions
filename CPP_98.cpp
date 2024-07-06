int count_upper(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if ((i % 2 == 0 && toupper(s[i]) == 'A') || 
            (i % 2 == 0 && toupper(s[i]) == 'E') || 
            (i % 2 == 0 && toupper(s[i]) == 'I') || 
            (i % 2 == 0 && toupper(s[i]) == 'O') || 
            (i % 2 == 0 && toupper(s[i]) == 'U')) {
            count++;
        }
    }
    return count;
}