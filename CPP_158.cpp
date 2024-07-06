vector<string> find_max(vector<string> words){
    vector<string> result = words;
    sort(result.begin(), result.end());
    int max_unique_chars = 0;
    string max_string = "";
    for (int i = 0; i < result.size(); i++) {
        unordered_set<char> unique_chars(result[i].begin(), result[i].end());
        if(unique_chars.size() > max_unique_chars) {
            max_unique_chars = unique_chars.size();
            max_string = result[i];
        }
    }
    return {max_string};
}