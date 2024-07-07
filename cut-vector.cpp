#include <vector>
using namespace std;

void cutVector(vector<int> v) {
    int min_diff = INT_MAX;
    vector<vector<int>> subvectors(2);
    
    for (int i = 1; i <= v.size() - 1; i++) {
        int left_sum = 0, right_sum = 0;
        for (int j = 0; j < i; j++) left_sum += v[j];
        for (int j = i; j < v.size(); j++) right_sum += v[j];
        
        if (left_sum == right_sum) {
            subvectors[0] = vector<int>(v.begin(), v.begin() + i);
            subvectors[1] = vector<int>(v.begin() + i, v.end());
            break;
        } else if (abs(left_sum - right_sum) < min_diff) {
            min_diff = abs(left_sum - right_sum);
            subvectors[0] = vector<int>(v.begin(), v.begin() + i);
            subvectors[1] = vector<int>(v.begin() + i, v.end());
        }
    }
    
    for (int i = 0; i < subvectors.size(); i++) {
        cout << "[";
        for (int j = 0; j < subvectors[i].size(); j++) {
            cout << subvectors[i][j];
            if (j != subvectors[i].size() - 1) cout << " ";
        }
        cout << "]" << endl;
    }
}

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }
    
    cutVector(v);
    
    return 0;
}