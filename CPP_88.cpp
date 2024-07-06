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
    int n1[] = {21, 14, 23, 11};
    int n2[] = {23, 21, 14, 11};
    std::vector<int> array1(n1, n1 + sizeof(n1) / sizeof(n1[0]));
    std::vector<int> array2(n2, n2 + sizeof(n2) / sizeof(n2[0]));
    assert (issame(array1, array2));
    sort_array(array1);
}