#include <vector>
using namespace std;

vector<int> findPair(vector<vector<int>>& pairs) {
    vector<int> result;
    int target = pairs[1][2];
    
    for(int i = 0; i < pairs.size() - 1; i++) {
        for(int j = i + 1; j < pairs.size(); j++) {
            if(pairs[i][1] + pairs[j][1] == target) {
                result.push_back(pairs[i][1]);
                result.push_back(pairs[j][1]);
                return result;
            }
        }
    }
    
    // If no pair is found
    result.push_back(-1);
    result.push_back(-1);
    return result;
}

int main() {
    int numPairs;
    cin >> numPairs;
    
    vector<vector<int>> pairs(numPairs);
    
    for(int i = 0; i < numPairs; i++) {
        cin >> pairs[i][0] >> pairs[i][1];
    }
    
    vector<int> result = findPair(pairs);
    
    cout << result[0] << "\n";
    cout << result[1] << "\n";
    
    return 0;
}