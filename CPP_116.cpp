bool issame(vector<vector<int>> a,vector<vector<int>> b){
    if(a.size()!=b.size()) return false;
    for(int i=0; i<a.size();i++){
        if(a[i][1] != b[i][1]) return false;
    }
    return true;
}
vector<int> sort_array(vector<int> arr){
    vector<int> result;
    for(int i: arr) {
        int ones = 0;
        int num = i;
        while(num > 0) {
            if((num & 1) == 1)
                ones++;
            num >>= 1;
        }
        result.push_back({ones, i});
    }
    sort(result.begin(), result.end());
    vector<int> res;
    for(auto x: result) {
        res.push_back(x.second);
    }
    return res;
}