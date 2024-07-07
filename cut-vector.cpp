#include <vector>
using namespace std;

pair<vector<int>, vector<int>> cutVector(vector<int> v) {
    int n = v.size();
    pair<vector<int>, vector<int>> res;
    
    for(int i=0; i<n-1; i++){
        if(abs(v[i]-v[i+1]) <= abs(v[0] - v[n-1])){
            res.first = v.substr(0, i+1);
            res.second = v.substr(i+1, n-i-1);
            break;
        }
    }
    
    else{
        res.first = v;
        res.second = vector<int>(0);
    }
    
    return res;
}

int main() {
    int n;
    cin >> n;
    vector<int> v(n);
    for(int i=0; i<n; i++) {
        cin >> v[i];
    }

    pair<vector<int>, vector<int>> res = cutVector(v);

    cout << "First part: ";
    for (int i : res.first) {
        cout << i << " ";
    }
    cout << endl;

    cout << "Second part: ";
    for (int i : res.second) {
        cout << i << " ";
    }
    cout << endl;
    
    return 0;
}