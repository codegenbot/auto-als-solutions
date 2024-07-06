int is_bored(string S) {
    int boredom_count = 0;
    string word;
    bool in_sentence = false;

    for (char c : S) {
        if (c == '.' || c == '?' || c == '!') {
            in_sentence = false;
        } else if (in_sentence) {
            word += c;
        } else if (word.size() > 0) {
            word = c == ' ' ? "" : c + " ";
            in_sentence = true;
        } else if (c == 'I' && c != ' ') {
            boredom_count++;
            in_sentence = true;
            word = c == ' ' ? "" : c + " ";
        }
    }

    return boredom_count;
}