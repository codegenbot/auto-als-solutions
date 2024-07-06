vector<string> sorted_list_sum(vector<string> lst) {
    vector<string> result;
    for (const auto& str : lst) {
        if (str.length() % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(), 
         [](const string& a, const string& b) {
             return a < b;
         });
    vector<string> sortedLst = lst;
    sort(sortedLst.begin(), sortedLst.end());
    for (const auto& str : result) {
        if (sortedLst != vector<string>(1, str)) {
            return {};
        }
    }
    return result;
}