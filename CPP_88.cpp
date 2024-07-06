```cpp
#include <vector>
#include <algorithm>
#include <tr1/initializer_list>

bool issame(std::vector<int> a, std::vector<int> b) {
    if(a.size()!=b.size()) return false;
    for(int i=0; i<a.size(); i++){
        if(a[i]!=b[b.size()-1-i]) return false;
    }
    return true;
}

int sort_array(std::vector<int>& array) {
    std::sort(array.begin(), array.end());
    return 0;
}

int main() {
    std::vector<int> array = {21, 14, 23, 11};
    std::vector<int> result = sort_array(array);
    assert(issame(result,{23,21,14,11}));
    return 0;
}