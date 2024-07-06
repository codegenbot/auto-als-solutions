int is_bored(string S) {
    int boredoms = 0;
    string word;
    for (char c : S + ".") {
        if (c == '.') {
            word.clear();
        } else if (c == '!' || c == '?') {
            if (!word.empty() && word[0] == 'I') {
                boredoms++;
            }
            word.clear();
        } else {
            word += c;
        }
    }
    return boredoms;
}