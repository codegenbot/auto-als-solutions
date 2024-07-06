#include <vector>
#include <algorithm>
#include <initializer_list>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) return false;
    for(int i = 0; i < a.size(); i++) {
        if (a[i] != b[b.size()-1-i]) return false;
    }
    return true;
}

int main() {
    std::vector<int> array1 = {21, 14, 23, 11};
    std::vector<int> array2 = {23, 21, 14, 11};
    assert (issame(array1, array2));
    // Sort and compare
    void sort_array(std::vector<int>& array) { 
        std::sort(array.begin(), array.end());
    }