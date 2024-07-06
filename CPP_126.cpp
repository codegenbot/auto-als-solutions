#include <vector>
#include <algorithm>

bool is_sorted(std::vector<int> lst) {
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i - 1] >= lst[i]) {
            return false;
        }
    }
    auto last = std::unique(lst.begin(), lst.end());
    return last == lst.end();
}

int main() {
    assert(is_sorted({1, 2, 3, 4}) == true);
    // Add more test cases or program logic here
    return 0;
}