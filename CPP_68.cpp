#include <vector>

using namespace std;

vector<vector<int>> pluck(vector<int>& arr) {
    vector<int> result;
    if (arr.empty()) return {{}};
    
    int minEvenIndex = -1;
    int minEvenValue = INT_MAX;
    
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < minEvenValue) {
            minEvenValue = arr[i];
            minEvenIndex = i;
        }
    }
    
    if (minEvenIndex != -1) {
        result = {{minEvenValue, minEvenIndex}};
    } else {
        result = {{}};
    }
    
    return result;
}