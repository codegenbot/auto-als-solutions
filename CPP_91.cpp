int is_bored(string S){
    int boredoms = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != string::npos) {
        if (S[pos] == ' ' || pos == 0) {
            if (pos + 1 < S.length() && (S[pos+1] == '.' || S[pos+1] == '?' || S[pos+1] == '!')) {
                boredoms++;
            }
            break;
        }
        pos++;
    }
    return boredoms;
}