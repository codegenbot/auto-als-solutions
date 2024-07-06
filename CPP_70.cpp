#include <vector>
#include <algorithm>

bool issame(vector<int> a, vector<int> b) {
    return a == b;
}

vector<int> strange_sort_list(vector<int> lst) {
    vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
        
        if (!lst.empty()) {
            int max_val = *max_element(lst.begin(), lst.end());
            result.push_back(max_val);
            for(int i : lst) {
                if(i == max_val) {
                    lst.erase(remove(lst.begin(), lst.end(), i), lst.end());
                    break;
                }
            }
        } else {
            result.push_back(*min_element(lst.begin(), lst.end()));
        }
    }
    return result;
}