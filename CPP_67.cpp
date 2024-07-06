int fruit_distribution(string s, int n) {
    size_t pos = 0;
    int apples = 0, oranges = 0;
    
    while ((pos = s.find(" apples", pos)) != string::npos) {
        apples += stoi(s.substr(pos + 7).erase(0, 1));
        s.erase(0, pos + 8);
    }
    
    while ((pos = s.find(" oranges")) != string::npos) {
        oranges += stoi(s.substr(pos + 8).erase(0, 1));
        s.erase(0, pos + 9);
    }
    
    return n - apples - oranges;
}