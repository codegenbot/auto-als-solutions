```cpp
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

std::vector<int> strange_sort_list(std::vector<int> lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
        if (!lst.empty()) {
            vector<int> temp;
            for(int i : lst){
                if(i == *max_element(lst.begin(), lst.end())){
                    temp.push_back(i);
                    break;
                }
            }
            for(int x:temp){
                lst.erase(remove(lst.begin(), lst.end(), x), lst.end());
            }
            result.push_back(*max_element(lst.begin(), lst.end()));
        } else {
            result.push_back(*min_element(lst.begin(), lst.end()));
        }
    }
    return result;
}

int main() {
    std::vector<int> input; // get your input here
    std::cout << "Enter elements separated by spaces: ";
    for (int i = 0; i < 5; ++i) {
        int num;
        std::cin >> num;
        input.push_back(num);
    }
    std::vector<int> result = strange_sort_list(input);
    std::cout << "Sorted List: ";
    for (int i : result)
        std::cout << i << " ";
    return 0;
}