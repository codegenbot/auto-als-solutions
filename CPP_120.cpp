vector<int> maximum(vector<int> arr,int k){
    vector<int> res(k);
    partial_sort(res.begin(), res.end(), [&arr](int a, int b) { return arr.count(a) > arr.count(b); });
    return res;
}