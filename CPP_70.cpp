```cpp
#include <vector>
#include <algorithm>

bool std::issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

std::vector<int> strange_sort_list(std::vector<int> lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int val = *lst.begin();
        result.push_back(val);
        lst.erase(remove(lst.begin(), lst.end(), val), lst.end());
        if (!lst.empty()) {
            std::vector<int> temp;
            for(int i : lst){
                if(i == *std::max_element(lst.begin(), lst.end())){
                    temp.push_back(i);
                    break;
                }
            }
            for(int x:temp){
                lst.erase(remove(lst.begin(), lst.end(), x), lst.end());
            }
            result.push_back(*std::max_element(lst.begin(), lst.end()));
        } else {
            result.push_back(*std::min_element(lst.begin(), lst.end()));
        }
    }
    return result;
}