int fruit_distribution(string s) {
    int n = stoi(s);
    size_t pos = 0;
    string input = s;
    int apples = 0;
    int oranges = 0;

    while ((pos = input.find(" ")) != string::npos) {
        if (input.substr(0, pos).find("apples") != string::npos)
            apples = stoi(input.substr(0, pos).substr(input.find(" ") + 1));
        else if (input.substr(0, pos).find("oranges") != string::npos)
            oranges = stoi(input.substr(0, pos).substr(input.find(" ") + 1));
        input.erase(0, pos + 1);
    }

    return n - apples - oranges;
}