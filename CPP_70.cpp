#include <iostream>
#include <algorithm>
#include <vector>

bool issame(std::vector<int> a,std::vector<int>b){
    if(a.size() != b.size()) return false;
    for(int i = 0; i<a.size(); i++){
        if(a[i] != b[i]) return false;
    }
    return true;
}

std::vector<int> strange_sort_list(std::vector<int> lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min = *std::min_element(lst.begin(), lst.end());
        result.push_back(min);
        lst.erase(std::remove(lst.begin(), lst.end(), min), lst.end());
        if (!lst.empty())
            result.push_back(*std::max_element(lst.begin(), lst.end()));
        lst.erase(std::remove(lst.begin(), lst.end(), *std::max_element(lst.begin(), lst.end())), lst.end());
    }
    return result;
}

int main() {
    assert(issame(strange_sort_list({111111}) , {111111}));
    return 0;
}