string findMax(vector<string> words){
    string result = *max_element(words.begin(), words.end(),
        [](const string& a, const string& b) {
            int unique_a = a.size() - unique(cout << a, (int)set<char>());
            int unique_b = b.size() - unique(cout << b, (int)set<char>());
            return unique_a > unique_b;
        });
    return result;
}