#include <vector>
#include <algorithm>

bool sameHelper(const std::vector<std::pair<int, int>>& a, const std::vector<stdstd::pair<int, int>>& b) {
    if (a.size() != b.size()) return false;
    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

std::vector<int> extract(std::vector<int> arr) {
    std::vector<std::pair<int, int>> nodes;
    for (int i = 0; i < arr.size(); ++i) {
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
        if (sameHelper({nodes[i-1].first, nodes[i-1].second}, {nodes[i].first, nodes[i].second})) {
            return {};
        }
    }
    
    return {nodes[0].first};
}