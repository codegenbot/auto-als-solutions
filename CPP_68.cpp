#include <vector>
#include <climits>

using namespace std;

vector<pair<int, int>> pluck(vector<int> arr) {
    vector<pair<int, int>> result;
    
    if(arr.empty()) return result; 
    
    int smallestEven = INT_MAX; 
    int smallestIndex = 0;
    
    for(int i = 0; i < arr.size(); i++) {
        if(arr[i] % 2 == 0 && arr[i] < smallestEven) {
            smallestEven = arr[i];
            smallestIndex = i;
        }
    }
    
    result.push_back({smallestEven, smallestIndex});
    
    return vector<pair<int, int>>({make_pair(smallestEven, smallestIndex)});
}