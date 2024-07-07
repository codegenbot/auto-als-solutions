#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool issame(vector<int> a, vector<int> b) {
    if(a.size()!=b.size()) return false;
    for(int i=0; i<a.size(); i++)
        if(a[i]!=b[i]) return false;
    return true;
}

vector<vector<int>> strange_sort_list(vector<int> lst) {
    vector<vector<int>> result;

    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        vector<int> temp;
        for(int i=0; i<lst.size(); i++) {
            if(*lst.rbegin()==*lst.begin()) {
                temp.push_back(min_val);
                lst.erase(std::remove(lst.begin(), lst.end(), min_val), lst.end());
                break;
            }
            else if (*lst[i] == min_val) {
                temp.push_back(min_val);
                lst.erase(std::remove(lst.begin(), lst.end(), min_val), lst.end());
            }
        }

        result.push_back(temp);

        while (!lst.empty()) {
            int max_val = *max_element(lst.begin(), lst.end());
            vector<int> temp;
            for(int i=0; i<lst.size(); i++) {
                if(*lst.rbegin()==*lst.begin()) {
                    temp.push_back(max_val);
                    lst.erase(std::remove(lst.begin(), lst.end(), max_val), lst.end());
                    break;
                }
                else if (*lst[i] == max_val) {
                    temp.push_back(max_val);
                    lst.erase(std::remove(lst.begin(), lst.end(), max_val), lst.end());
                }
            }

            result.push_back(temp);

            if (!lst.empty()) {
                min_val = *min_element(lst.begin(), lst.end());
                max_val = *max_element(lst.begin(), lst.end());

                while (min_val != max_val) {
                    if (*min_element(lst.begin(), lst.end()) < *max_element(lst.begin(), lst.end())) {
                        temp.push_back(min_val);
                        lst.erase(std::remove(lst.begin(), lst.end(), min_val), lst.end());
                    }
                    else {
                        temp.push_back(max_val);
                        lst.erase(std::remove(lst.begin(), lst.end(), max_val), lst.end());
                    }

                    result.push_back(temp);
                }
            }
        }
    }

    return result;
}

int main() {
    assert(issame(strange_sort_list({111111}) , {111111}));
    return 0;
}