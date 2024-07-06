```cpp
#include <algorithm>
#include <vector>

std::vector<int> strange_sort_list(std::vector<int> lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min_val = *std::min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(std::remove(lst.begin(), lst.end(), min_val), lst.end());
        
        if (!lst.empty()) {
            vector<int> temp;
            for(int i : lst){
                if(i == *std::max_element(lst.begin(), lst.end())){
                    temp.push_back(i);
                    break;
                }
            }
            for(int x:temp){
                lst.erase(std::remove(lst.begin(), lst.end(), x), lst.end());
            }
            result.push_back(*std::max_element(lst.begin(), lst.end()));
        } else {
            result.push_back(*std::min_element(lst.begin(), lst.end()));
        }
    }
    return result;
}

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return (a.size() == b.size()) && std::all_of(a.begin(), a.end(),
        [&b](int x) {return std::find(b.begin(), b.end(), x) != b.end();});
}

#include <cassert>

int main() {
    assert(issame(strange_sort_list({111}), std::vector<int>{111}));
    return 0;
}