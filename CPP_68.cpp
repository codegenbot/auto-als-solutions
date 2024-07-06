```
#include <vector>
#include <algorithm>
#include <initializer_list>

bool compare(const std::pair<int, int>& a, const std::pair<int, int>& b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second < b.second;
}

int main() {
    std::vector<int> arr = {7, 9, 7, 1};
    std::vector<int> result = pluck(arr);
    assert(result.empty());
    return 0;
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