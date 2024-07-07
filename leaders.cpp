#include <vector>
#include <algorithm>
using namespace std;

vector<int> leaders(vector<int>& arr) {
    int n = arr.size();
    vector<int> result;
    
    if(n == 1) return {arr[0]};
    
    result.push_back(arr[n-1]);
    
    for(int i=n-2; i>=0; i--) {
        while(i<n-1 && arr[i] >= arr[i+1]) {
            i--;
        }
        if(i == -1) break;
        result.push_back(arr[i]);
    }
    
    return result;
}