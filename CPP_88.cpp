#include <initializer_list>

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
    return array;
}

int main() {
    std::vector<int> array1 = {21, 14, 23, 11};
    std::vector<int> array2 = {23, 21, 14, 11};
    assert (issame(array1, array2));
    array1 = sort_array(array1); 
    if (!issame(array1, std::vector<int>({23, 21, 14, 11}))) {
        std::cout << "Arrays are not same." << std::endl;
    }
}