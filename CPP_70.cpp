#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> strange_sort_list(vector<int> lst) {
    vector<int> result;
    
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        int max_val = *max_element(lst.begin(), lst.end());
        
        if (min_val < max_val) {
            result.push_back(min_val);
            lst.erase(std::remove(lst.begin(), lst.end(), min_val), lst.end());
        } else {
            result.push_back(max_val);
            lst.erase(std::remove(lst.begin(), lst.end(), max_val), lst.end());
        }
    }
    
    return result;
}

int main() {
    vector<int> test_cases = {{1, 2, 3, 4}, {5, 5, 5, 5}, {}};
    
    for (auto& test_case : test_cases) {
        auto result = strange_sort_list(test_case);
        
        cout << "Test case: ";
        for (int val : test_case) {
            cout << val << " ";
        }
        cout << endl;
        
        cout << "Result: ";
        for (int val : result) {
            cout << val << " ";
        }
        cout << endl;
        cout << endl;
    }
    
    return 0;
}