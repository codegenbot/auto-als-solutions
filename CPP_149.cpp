```
vector<string> sorted_list_sum(vector<string> lst) {
    vector<string> result;
    for (const auto& str : lst) {
        if (stoi(str) % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(),
         [](const string& a, const string& b) {
             if (stoi(a) != stoi(b)) {
                 return stoi(a) < stoi(b);
             } else {
                 return a < b;
             }
         });
    return result;
}