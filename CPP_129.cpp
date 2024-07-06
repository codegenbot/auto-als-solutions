int minPath(vector<vector<char>>& grid, int x, int y, vector<pair<int, int>>& path) {
    if(x<0 || y<0 || x>=grid.size() || y>=grid[0].size())
        return -1;
    
    if(grid[x][y]=='E')
        return 1;

    if(grid[x][y]=='#') 
        return -1;

    int res = -1;
    grid[x][y]='#';
    
    for(int i=-1; i<=1; i++){
        for(int j=-1; j<=1; j()){
            if(i==0 && j==0) continue;
            if(x+i>=0 && x+i<grid.size() && y+j>=0 && y+j<grid[0].size())
                res = max(res, minPath(grid, x+i, y+j, path));
        }
    }

    grid[x][y]=0;

    return res;
}

bool isEqual(vector<int> a,vector<int>b){
    return a==b;
}