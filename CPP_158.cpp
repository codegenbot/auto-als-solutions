string find_max(vector<string> words){
    string result = *max_element(words.begin(), words.end(),
        [](const string& a, const string& b) {
            if (a.size() == b.size()) {
                return a < b;
            }
            return a.size() > b.size();
        });
    for (string word : words) {
        if (word.size() >= result.size()) {
            int unique_chars_a = 0, unique_chars_b = 0;
            set<char> set_a(word.begin(), word.end());
            for (char c : set_a) {
                unique_chars_a++;
            }
            set<char> set_b(result.begin(), result.end());
            for (char c : set_b) {
                unique_chars_b++;
            }
            if (unique_chars_a > unique_chars_b) {
                result = word;
            }
        }
    }
    return result;
}