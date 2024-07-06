Here is the completed code:

```cpp
string find_max(vector<string> words){
    string max_word = *max_element(words.begin(), words.end(),
        [](const string& a, const string& b) {
            if (a.size() == b.size()) {
                return a < b;
            }
            return a.size() > b.size();
        });
    
    map<char, int> char_count;
    for (char c : max_word) {
        char_count[c]++;
    }
    
    int max_unique = 0;
    for (auto p : char_count) {
        if (p.second == 1) {
            max_unique++;
        }
    }
    
    return max_word;
}