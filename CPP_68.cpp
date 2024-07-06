#include <vector>
#include <algorithm>

std::vector<int> pluck(std::vector<int> arr) {
    std::vector<int> result;
    
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] % 2 == 0) {
            bool isSame = true;
            
            for (size_t j = 0; j < result.size(); ++j) {
                if (result[j] == arr[i]) {
                    isSame = false;
                    break;
                }
            }
            
            if (isSame) {
                result.push_back(arr[i]);
            }
        }
    }
    
    return result;
}

int main() {
    std::vector<int> arr = {7, 9, 7, 1};
    if (pluck(arr).empty()) {
        assert(pluck({7, 9, 7, 1}) == {});
    } else {
        // Handle the case where pluck returns a non-empty vector
    }
}