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
    
    vector<int> result = {evenNodes[0].first};
    for (int i = 1; i < evenNodes.size(); i++) {
        if (issame(result, vector<int>(result.begin() + 1, result.end()))) {
            break;
        }
        result.push_back(evenNodes[i].first);
    }
    
    return result;
}