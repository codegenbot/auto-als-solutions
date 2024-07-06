#include <iostream>
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

std::vector<int> strange_sort_list(std::vector<int> lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        
        // Remove all occurrences of `min_val` before moving on to `max_val`
        while (lst.size() > 0 && *std::min_element(lst.begin(), lst.end()) == min_val) {
            lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
        }
        
        if (!lst.empty()) {
            int max_val = *max_element(lst.begin(), lst.end());
            
            // Remove all occurrences of `max_val` after moving on to the next element
            while (lst.size() > 0 && *std::min_element(lst.begin(), lst.end()) == max_val) {
                lst.erase(remove(lst.begin(), lst.end(), max_val), lst.end());
            }
            
            result.push_back(max_val);
        } else {
            int min_val2 = *min_element(lst.begin(), lst.end());
            result.push_back(min_val2);
        }
    }
    
    return result;
}

int main() {
    std::vector<int> input;  // get your input here
    std::cout << "Enter elements of the vector separated by space: ";
    for (int i = 0; i < 5; ++i) {
        int num;
        std::cin >> num;
        input.push_back(num);
    }
    
    std::vector<int> result = strange_sort_list(input);
    std::cout << "The sorted list is: ";
    for (int i : result) {
        std::cout << i << " ";
    }
    return 0;
}