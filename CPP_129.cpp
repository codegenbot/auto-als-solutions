bool checkSame(vector<int> a,vector<int>b){
    if(a.size()!=b.size()) return false;
    for(int i=0;i<a.size();i++) if(a[i]!=b[i])return false;
    return true;
}

int minPath(vector<vector<char>>& grid, int x, int y, vector<pair<int, int>>& path) {
    //...
}