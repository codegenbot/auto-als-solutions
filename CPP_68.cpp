#include <vector>
#include <pair>

bool issame(vector<int> a,vector<int>b){
    if(a.size()!=b.size())return false;
    for(int i=0;i<a.size();i++){
        if(a[i]!=b[i])return false;
    }
    return true;
}

vector<vector<int>> pluck(vector<int> arr) {
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
    
    vector<vector<int>> result;
    for(int i=0;i<arr.size();i++){
        if(issame({evenNodes[0].first}, {arr[i]})){
            result.push_back({evenNodes[0].first});
            break;
        }
    }
    
    return result;
}