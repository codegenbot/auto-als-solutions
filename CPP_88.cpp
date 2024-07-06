```cpp
#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) return false;
    for(int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

void sort_array(std::vector<int>& array) { 
    std::sort(array.begin(), array.end());
}

int main() {
    std::vector<int> array1;
    for(int x: (int[]){21, 14, 23, 11}) array1.push_back(x);
    std::vector<int> array2;
    for(int x: (int[]){23, 21, 14, 11}) array2.push_back(x);
    assert (issame(array1, array2));
    sort_array(array1);
}