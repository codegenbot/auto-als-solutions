#include <vector>
using namespace std;

vector<int> findPair(vector<int>& arr, int target) {
    unordered_map<int, int> map;
    vector<int> result;
    
    for(int i = 0; i < arr.size(); i++) {
        int comp = target - arr[i];
        if(map.find(comp) != map.end()) {
            result.push_back(arr[i]);
            result.push_back(comp);
            break;
        }
        map[arr[i]] = i;
    }
    
    return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int target;
    cin >> target;
    vector<int> res = findPair(arr, target);
    cout << res[0] << endl << res[1] << endl;
    
    return 0;
}