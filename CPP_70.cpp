#include <iostream>
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

void strange_sort_list(const std::vector<int>& lst) {
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
    std::vector<int> input;
    std::cout << "Enter elements of the vector separated by space: ";
    for (int i = 0; i < 5; ++i) {
        int num;
        std::cin >> num;
        input.push_back(num);
    }
    
    strange_sort_list(input); 
    return 0;
}