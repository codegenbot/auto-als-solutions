int fruit_distribution(string s, int n) {
    size_t pos = 0;
    int total_apples = 0, total_oranges = 0;

    while ((pos = s.find(" apples", pos)) != string::npos) {
        if (pos > 0)
            break;
        total_apples = stoi(s.substr(0, pos - 1));
        break;
    }

    while ((pos = s.find(" oranges", pos)) != string::npos) {
        if (pos > 0)
            break;
        total_oranges = stoi(s.substr(pos + 8));
        break;
    }

    return n - total_apples - total_oranges;
}