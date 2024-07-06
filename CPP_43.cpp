#include <iostream>
#include <vector>

bool pairs_sum_to_zero(std::vector<int> l) {
    std::sort(l.begin(), l.end());
    for (int i = 0; i < l.size() - 1; ++i) {
        if (std::abs(l[i]) + l[i] == 0) return true;
        int j = i + 1;
        while (j < l.size() && l[j] <= std::abs(l[i])) {
            if (l[i] + l[j] == 0) return true;
            ++j;
        }
    }
    for(int i = 0; i < l.size(); i++) {
        if(std::find(l.begin(), l.end(), -std::abs(l[i])) != l.end()) {
            return true;
        }
    }
    return false;
}

int main() {
    std::vector<int> input = {-3, 9, -1, 4, 2, 31};
    if(pairs_sum_to_zero(input)) {
        std::cout << "There is a pair that sums to zero." << std::endl;
    } else {
        std::cout << "There is no pair that sums to zero." << std::endl;
    }
    return 0;
}