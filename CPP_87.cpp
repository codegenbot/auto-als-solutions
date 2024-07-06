#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x) {
    vector<vector<int>> result;
    
    for(int i = 0; i < lst.size(); i++) {
        if(lst[i].size() > 0) {
            for(int j = 0; j < lst[i].size(); j++) {
                if(lst[i][j] == x) {
                    result.push_back({i, j});
                }
            }
        }
    }
    
    // Sort the coordinates by rows in ascending order
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] < b[0];
    });
    
    // Sort the coordinates of each row by columns in descending order
    for(auto& coord : result) {
        sort(coord.begin(), coord.end(), greater<int>());
    }
    
    return result;
}

int main() {
    vector<vector<int>> lst = {{1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 1, 6}, {1, 2, 3, 4, 5, 1}};
    int x = 1;
    
    vector<vector<int>> result = get_row(lst, x);
    
    for(auto& coord : result) {
        cout << "{" << coord[0] << ", " << coord[1] << "} ";
    }
    cout << endl;
    
    return 0;
}