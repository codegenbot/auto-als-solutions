```cpp
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> arr = {7, 9, 7, 1};
    if (pluck(arr).empty()) {
        return 0;
    } else {
        for (int num : pluck(arr)) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
}

std::vector<int> pluck(std::vector<int> arr) {
    std::vector<std::pair<int, int>> nodes;
    for (size_t i = 0; i < arr.size(); ++i) {
        if (arr[i] % 2 == 0) {
            nodes.push_back({arr[i], i});
        }
    }
    
    if (nodes.empty()) {
        return {};
    }
    
    std::sort(nodes.begin(), nodes.end());
    
    std::vector<int> result;
    for (size_t i = 1; i < nodes.size(); ++i) {
        if (nodes[i-1].first == nodes[i].first) {
            return {};
        }
    }
    
    for (const auto& node : nodes) {
        result.push_back(node.first);
    }
    
    return result;
}