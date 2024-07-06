int is_bored(string S) {
    int count = 0;
    string boredom = "I";
    size_t start = 0;
    while ((start = S.find(" ", start)) != string::npos) {
        if (S.substr(0, start).compare(boredom) == 0) {
            count++;
        }
        start += 1;
    }
    return count;
}