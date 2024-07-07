```cpp
#include <vector>
bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

int main() {
    int k = 5; // You should replace this with the desired value of k.
    vector<int> arr = {1,2,3,4,5};
    try {
        vector<int> res = maximum(arr,k);
        for(auto x : res) {
            cout << x << " ";
        }
        cout << endl;
    }catch(const exception& e){
        cerr << "Error: " << e.what() << endl;
    }
    return 0;
}

vector<int> maximum(vector<int> arr,int k){
    if(k == 0) throw runtime_error("k cannot be zero");
    vector<int> res(k);
    partial_sort(res.begin(), res.end(), [&arr](int a, int b) { return arr.count(a) > arr.count(b); });
    return res;
}