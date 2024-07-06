```cpp
#include <vector>
#include <algorithm>

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
    
    void sort_array(std::vector<int>& array) { 
        std::sort(array.begin(), array.end());
    }
    sort_array(array1);
    sort_array(array2);
    
    if (!issame(array1, array2)) {
        for(int i = 0; i < array1.size(); i++) {
            if (array1[i] > array2[i]) {
                std::cout << "First different element is: " << array1[i] << "\n";
                return;
            }
        }
    } else {
        std::cout << "Arrays are the same\n";
    }
}