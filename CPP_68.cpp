#include <vector>
#include <pair>

bool issame(vector<int> a,vector<int>b){
    if(a.size()!=b.size())return false;
    for(int i=0;i<a.size();i++){
        if(a[i]!=b[i])return false;
    }
    return true;
}

vector<vector<int>> pluck(vector<vector<int>> arr) {
    vector<pair<int, int>> evenNodes;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr[i].size(); j++) {
            if (arr[i][j] % 2 == 0) {
                evenNodes.emplace_back(arr[i][j], i);
            }
        }
    }
    
    if (evenNodes.empty()) {
        return {};
    }
    
    sort(evenNodes.begin(), evenNodes.end());
    
    vector<vector<int>> result;
    for(int i=0;i<arr.size();i++){
        bool same = false;
        for(int j=0;j<arr[i].size();j++){
            if(find(evenNodes.begin(),evenNodes.end(),make_pair(arr[i][j],i))!=evenNodes.end()){
                same=true;break;
            }
        }
        if(same)result.push_back(arr[i]);
    }
    
    return result;
}