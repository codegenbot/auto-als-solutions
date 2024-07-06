int count_upper(string s){
    int count = 0;
    for(int i = 1; i < s.length(); i += 2) {
        string c = s.substr(i, 1);
        if(toupper(c[0]) == 'A' || toupper(c[0]) == 'E' || toupper(c[0]) == 'I' || toupper(c[0]) == 'O' || toupper(c[0]) == 'U') {
            count++;
        }
    }
    return count;
}