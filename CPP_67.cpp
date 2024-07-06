int fruit_distribution(string s, int n) {
    int total_apples = 0;
    int total_oranges = 0;

    size_t pos = 0;
    while ((pos = s.find(" apples")) != string::npos) {
        total_apples += (stoi(s.substr(0, pos).erase(0, 1)) + stoi(s.substr(pos + 9)));
        pos = s.find(" apples", pos + 11); 
    }

    if ((pos = s.find(" oranges")) != string::npos) {
        total_oranges = stoi(s.substr(0, pos).erase(0, 7));
    }

    return max(n - (total_apples + total_oranges), 0);
}