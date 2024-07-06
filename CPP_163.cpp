```cpp
#include <vector>
#include <algorithm>

std::vector<int> generate_integers(int a, int b) {
    std::vector<std::vector<int>> result;
    for (int i = std::min(a, b); i <= std::max(a, b); i++) {
        if (i % 2 == 0) {
            result.push_back({i});
        }
    }
    return result;
}

bool operator==(const std::vector<int>& a,const std::vector<int>&b){
    if(a.size()!=b.size())
        return false;
    for(int i=0;i<a.size();i++){
        if(a[i]!=b[i])
            return false;
    }
    return true;
}

int main_test() { 
    assert(std::equal(generate_integers(17,89).begin(), generate_integers(17,89).end(), (int []){}));
    return 0;
}