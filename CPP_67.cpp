int fruit_distribution(string s, int n) {
    size_t pos = 0;
    int apples = 0, oranges = 0;
    
    while ((pos = s.find(" apples", pos)) != string::npos) {
        apples = stoi(s.substr(0, pos).erase().substr(1).erase());
        pos += 7; // Update position for next search
    }
    
    if (s.find(" oranges") != string::npos) {
        size_t temp = s.find(" oranges");
        while (temp != string::npos) {
            oranges = stoi(s.substr(temp + 8).erase());
            temp = s.find(" oranges", temp + 1);
        }
    }
    
    return n - apples - oranges;
}