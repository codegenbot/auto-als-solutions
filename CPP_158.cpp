Here is the solution:

```cpp
string find_max(vector<string> words){
    string max_str = *max_element(words.begin(), words.end(),
        [](const string& a, const string& b) {
            if (a.length() == b.length()) {
                return a < b;
            }
            return a.length() > b.length();
        });
    for (string s : words) {
        if (s.length() > max_str.length() || (s.length() == max_str.length() && s < max_str)) {
            max_str = s;
        }
    }
    return max_str;
}