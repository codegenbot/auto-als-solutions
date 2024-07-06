bool isEqual(std::vector<int> a, std::vector<int> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}

int pathFinder(std::vector<std::vector<char>> grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if(x<0 || y<0 || x>=grid.size() || y>=grid[0].size()) 
        return 0; 

    if(grid[x][y] == '#') 
        return 1; 

    grid[x][y] = '#'; 

    for(int i=-1;i<=1;i++) {
        for(int j=-1;j<=1;j++) { 
            int newX = x + i;
            int newY = y + j; 
            if(newX>=0 && newX<grid.size() && newY>=0 && newY<grid[0].size()) {
                if(isPath(grid, newX, newY)) {
                    std::pair<int,int> p = std::make_pair(newX,newY);
                    path.push_back(p); 
                    int res = 1 + pathFinder(grid, newX, newY,path); 
                    if(res > 0) 
                        return res; 
                }
            }  
        }
    }

    grid[x][y] = '.'; 

    return 0;
}