int max_fill(vector<vector<int>> grid, int capacity) {
    int rows = grid.size();
    int cols = grid[0].size();
    int result = 0;
    
    for(int i=0; i<rows; i++){
        int water = 0;
        for(int j=0; j<cols; j++){
            water += grid[i][j];
        }
        while(water > 0){
            if(capacity <= water){
                result += (water / capacity);
                water %= capacity;
            }else{
                result++;
                water -= capacity;
            }
        }
    }
    
    return result;
}