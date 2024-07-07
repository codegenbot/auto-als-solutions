#include <vector>
#include <algorithm>

bool issame(const vector<int>& a, const vector<int>& b) {
    return a == b;
}

vector<int> maximum(vector<int> arr,int k){
    if(k<1 || k >arr.size()) {
        throw runtime_error("Invalid value for k. It should be between 1 and the size of the array.");
    }
    vector<int> res(k);
    partial_sort(res.begin(), min(res.end(), arr.end()), [&arr](int a, int b) { return count(arr.begin(), arr.end(), a) > count(arr.begin(), arr.end(), b); });
    return res;
}