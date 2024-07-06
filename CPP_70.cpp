```cpp
#include <vector>
#include <algorithm>
using namespace std;

bool same(vector<int> a,vector<int>b){
    if(a.size() != b.size()) return false;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    for(int i = 0; i < a.size(); i++){
        if(a[i] != b[i]) return false;
    }
    return true;
}

vector<int> strange_sort_list(vector<int> lst) {
    vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
    }
    return result;
}