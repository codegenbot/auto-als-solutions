```cpp
#include <vector>
bool issame(const vector<int>& a, const vector<int>& b) {
    return a == b;
}
vector<int> maximum(vector<int> arr,int k){
    if(k <= 0) {
        throw runtime_error("k must be greater than zero");
    }
    vector<int> res(k);
    partial_sort(res.begin(), res.end(), [&arr](int a, int b) { return arr.count(a) > arr.count(b); });
    return res;
}