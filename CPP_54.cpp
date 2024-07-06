```cpp
bool same_chars(string s0, string s1) {
    return unique(s0.begin(), s0.end()) - s0.begin() == unique(s1.begin(), s1.end()) - s1.begin();
}