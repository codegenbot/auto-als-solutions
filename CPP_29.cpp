bool issame(string a, string b) {
    vector<string> filter(vector<string> strings, string prefix) {
        vector<string> result;
        for (string s : strings) {
            if (s.find(prefix) == 0)
                result.push_back(s);
        }
        return result;
    }