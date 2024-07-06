#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> get_row(vector<vector<int>> lst, int x) {
    int max_sum = 0;
    int max_index = -1;
    for (int i = 0; i < lst.size(); ++i) {
        int current_sum = 0;
        for (int j = 0; j < lst[i].size(); ++j) {
            current_sum += lst[i][j];
        }
        if (current_sum > max_sum) {
            max_sum = current_sum;
            max_index = i;
        }
    }
    vector<vector<int>> result = {{max_index, x}};
    return result;
}