#include <vector>

bool isSame(const std::vector<int>& vec) {
    if (vec.size() == 0) {
        return true;
    }
    
    int first = vec[0];
    for (int i = 1; i < vec.size(); i++) {
        if (vec[i] != first) {
            return false;
        }
    }
    
    return true;
}