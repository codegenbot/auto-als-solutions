int is_bored(string S){
    int count = 0;
    string word;

    for(size_t i = 0; i < S.size(); ++i) {
        if(S[i] == '.' || S[i] == '?' || S[i] == '!') {
            word = S.substr(0, i);

            if(word.size() > 1 && word[0] == 'I' && tolower(word[1]) != ' ') {
                count++;
            }

            S = S.substr(i + 1);
            i = -1;
        }
    }

    return count;
}