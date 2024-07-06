Here is the completed code:

vector<string> sorted_list_sum(vector<string> lst) {
    auto it = lst.begin();
    while (it != lst.end()) {
        if (it->length() % 2 == 1) {
            lst.erase(it);
            if (it == lst.begin())
                it = lst.begin();
            else
                it--;
        } else {
            it++;
        }
    }
    sort(lst.begin(), lst.end(),
         [](const string& a, const string& b) {
             if (a.length() != b.length()) {
                 return a.length() < b.length();
             } else {
                 return a < b;
             }
         });
    return lst;
}