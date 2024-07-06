int fruit_distribution(string s, int n) {
    size_t pos = 0;
    string word;
    int apples = 0, oranges = 0;

    while ((pos = s.find(" and ")) != string::npos) {
        word = s.substr(0, pos);
        if (word.find("apples") != string::npos)
            apples = stoi(word.substr(0, word.find(" ")));
        else if (word.find("oranges") != string::npos)
            oranges = stoi(word.substr(0, word.find(" ")));

        s.erase(0, pos + 5);
    }

    int mangoes = n - apples - oranges;
    return mangoes;
}