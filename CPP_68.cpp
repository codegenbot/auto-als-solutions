```cpp
#include <initializer_list>
#include <vector>
#include <algorithm>

bool compare(const std::pair<int, int>& a, const std::pair<int, int>& b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second < b.second;
}

std::vector<int> pluck(std::vector<int> arr) {
    std::vector<std::pair<int, int>> nodes;
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] % 2 == 0) {
            nodes.push_back({arr[i], i});
        }
    }
    
    if (nodes.empty()) {
        return {};
    }
    
    std::sort(nodes.begin(), nodes.end(), compare);
    
    std::vector<int> result;
    for (size_t i = 1; i < nodes.size(); ++i) {
        if (compare({nodes[i-1].first, nodes[i-1].second}, {nodes[i].first, nodes[i].second}) == false) {
            return {};
        }
    }
    
    return {nodes[0].first};
}

int main() {
    std::vector<int> arr;
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cout << "Enter element " << i+1 << ": ";
        std::cin >> x;
        arr.push_back(x);
    }
    std::vector<int> result = pluck(arr);
    if(result.size() > 0)
    {
        std::cout << "The output is: " << *result.begin() << std::endl;
    }
    else
    {
        std::cout << "No output" << std::endl;
    }
    
    return 0;
}