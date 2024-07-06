#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) return false;
    for(int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

std::vector<int> sort_array(std::vector<int>& array) { 
    std::sort(array.begin(), array.end());
    return std::move(array);
}

int main() {
    std::vector<int> array1; 
    for (int i : {21, 14, 23, 11}) {
        array1.push_back(i);
    }
    std::vector<int> array2 = {23, 21, 14, 11};
    assert (issame(array1, array2));
    array1 = sort_array(std::move(array1)); 
}