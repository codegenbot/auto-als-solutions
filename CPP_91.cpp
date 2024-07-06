int is_bored(string S){
    int count = 0;
    string sentence;
    for (char c : S) {
        if (c == '.' || c == '?' || c == '!') {
            sentence = sentence.substr(1);
            if (sentence.find("I") == 0)
                count++;
            sentence.clear();
        } else {
            sentence += c;
        }
    }
    return count;
}