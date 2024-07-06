int fruit_distribution(string s, int n) {
    size_t pos = 0;
    int apples = 0, oranges = 0;
    
    while ((pos = s.find(" apples", pos)) != string::npos) {
        apples = stoi(s.substr(0, pos).erase().substr(1).erase());
        pos += 7; 
    }
    
    if (s.find(" oranges") != string::npos) {
        size_t pos2 = s.find(" oranges");
        while ((pos2 = s.find(" oranges", pos2)) != string::npos) {
            oranges = stoi(s.substr(pos2 + 8).erase());
            pos2 += 8; 
        }
    }
    
    return n - apples - oranges;
}