```cpp
bool issame(vector<string> a, vector<string> b) {
    if (a.size() != b.size())
        throw runtime_error("Vectors of different sizes");
    
    for (int i = 0; i < a.size(); i++) {
        if (find(b.begin(), b.end(), a[i]) == b.end())
            throw runtime_error("Vectors not the same");
    }
    return true;
}