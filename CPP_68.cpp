#include <vector>
#include <algorithm>

bool issame(vector<int> a, vector<int> b) {
    return a == b;
}

vector<int> pluck(vector<int> arr) {
    vector<pair<int, int>> evenNodes;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0) {
            evenNodes.emplace_back(arr[i], i);
        }
    }
    
    if (evenNodes.empty()) {
        return {};
    }
    
    sort(evenNodes.begin(), evenNodes.end());
    
    vector<int> result;
    for (int i = 0; i < arr.size(); i++) {
        bool found = false;
        for (auto& node : evenNodes) {
            if (node.second == i) {
                result.push_back(node.first);
                found = true;
                break;
            }
        }
        if (!found) {
            result.push_back(arr[i]);
        }
    }
    
    return result;
}