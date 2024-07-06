#include <vector>

int main() {
    std::vector<std::vector<int>> grid = {{1,0,0},{1,1,0},{0,0,0}};
    int capacity = 2;
    cout << max_fill(grid, capacity) << endl;
    return 0;
}

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

    return (total_water + capacity - 1) / capacity;
}