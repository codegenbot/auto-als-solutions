bool issame(vector<vector<int>> a,vector<vector<int>> b){
    if(a.size()!=b.size()) return false;
    for(int i=0; i<a.size();i++){
        if(a[i][1] != b[i][1]) return false;
    }
    return true;
}