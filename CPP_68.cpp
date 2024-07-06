#include <vector>
#include <pair>

bool issame(vector<int> a,vector<int>b){
    if(a.size() != b.size()) {
        return false;
    }
    for(int i = 0; i < a.size(); i++) {
        if(a[i] != b[i]) {
            return false;
        }
    }
    return true;
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
    if(evenNodes.size() > 1) {
        for(int i = 1; i < evenNodes.size(); i++) {
            if(!issame({evenNodes[i-1].first}, {evenNodes[i].first})) {
                result.push_back(evenNodes[i].first);
            }
        }
    }
    
    return result;
}