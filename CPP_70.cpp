```
#include <vector>
#include <algorithm>

using namespace std;

bool issame(vector<int> v1, vector<int> v2) {
    if (v1.size() != v2.size()) 
        return false;
    for (int i = 0; i < v1.size(); i++) {
        if (v1[i] != v2[i]) 
            return false;
    }
    return true;
}

vector<int> strange_sort_vector(vector<int> lst) {
    vector<int> result;
    if (lst.empty()) return result;

    int minVal = *min_element(lst.begin(), lst.end());
    int maxVal = *max_element(lst.begin(), lst.end());

    while (!lst.empty()) {
        auto itMin = std::find_if(lst.begin(), lst.end(),
            [minVal](int val) { return val == minVal; });
        if (itMin != lst.end()) {
            result.push_back(*itMin);
            lst.erase(itMin);
        }

        auto itMax = std::find_if(lst.begin(), lst.end(),
            [maxVal](int val) { return val == maxVal; });
        if (itMax != lst.end()) {
            result.push_back(*itMax);
            lst.erase(itMax);
        }
    }

    return result;
}

assert(issame(strange_sort_vector({111111}) , {111111}));