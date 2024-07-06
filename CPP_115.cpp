#include <vector>

int max_fill(vector<vector<int>> grid, int capacity) {
    int rows = grid.size();
    int cols = grid[0].size();
    int total_water = 0;
    
    for(int i=0; i<rows; i++){
        for(int j=0; j<cols; j++){
            if(grid[i][j] == 1){
                total_water += 1;
            }
        }
    }
    
    int max_fill = total_water / capacity;
    if (total_water % capacity != 0) {
        max_fill++;
    }
    return max_fill;
}

int main() {
    vector<vector<int>> grid = {{1, 0}, {1, 0}};
    int capacity = 2;
    cout << "Max Fill: " << max_fill(grid, capacity) << endl;
}