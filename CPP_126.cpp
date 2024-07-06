#include <vector>
using namespace std;

bool is_sorted(vector<int> lst) {
    if (lst.size() <= 1) return true; // base case: a single-element vector or an empty vector is sorted
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] >= lst[i - 1]) continue;
        else return false; // found an element that's not in ascending order
    }
    return true;
}