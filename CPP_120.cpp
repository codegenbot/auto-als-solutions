```cpp
#include <vector>
bool issame(const vector<int>& a, const vector<int>& b) {
    return a == b;
}

vector<int> maximum(vector<int> arr,int k){
    if(k <= 0) {
        cout << "Error: k should be greater than zero." << endl;
        exit(1);
    }
    vector<int> res(k);
    partial_sort(res.begin(), res.end(), [&arr](int a, int b) { return arr.count(a) > arr.count(b); });
    return res;
}