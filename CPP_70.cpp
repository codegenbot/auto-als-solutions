#include <vector>
#include <algorithm>

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

vector<int> strange_sort_list(vector<int> lst) {
    vector<int> result;
    while (!lst.empty()) {
        int min = *min_element(lst.begin(), lst.end());
        result.push_back(min);
        lst.erase(remove(lst.begin(), lst.end(), min), lst.end());
        if (!lst.empty())
            result.push_back(*max_element(lst.begin(), lst.end()));
        lst.erase(remove(lst.begin(), lst.end(), *max_element(lst.begin(), lst.end())), lst.end());
    }
    return result;
}