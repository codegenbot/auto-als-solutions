#include <iostream>
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

void strange_sort_list(std::vector<int>& lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min_val = *std::min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(std::remove(lst.begin(), lst.end(), min_val), lst.end());

        if (!lst.empty()) {
            int max_val = *std::max_element(lst.begin(), lst.end());
            std::vector<int> temp;
            for (int i : lst) {
                if (i == max_val) {
                    lst.erase(std::remove(lst.begin(), lst.end(), i), lst.end());
                    break;
                } else {
                    temp.push_back(i);
                }
            }
            result.insert(result.end(), temp.begin(), temp.end());
        } else {
            int min_val2 = *std::min_element(lst.begin(), lst.end());
            result.push_back(min_val2);
        }
    }
}

int main() {
    int vec[] = {111111};
    std::vector<int> vecVec(vec, vec + sizeof(vec)/sizeof(vec[0]));
    
    std::vector<int> inputCopy = vecVec;
    strange_sort_list(inputCopy);
    
    assert(issame(inputCopy , vecVec));
    
    return 0;
}