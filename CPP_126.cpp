```cpp
bool is_sorted(vector<int> lst) {
    if (lst.size() <= 1) return true; // base case: a single-element vector or an empty vector is sorted
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] >= lst[i - 1]) continue;
        if (count(lst.begin(), lst.end(), lst[i]) > 1) return false; // found a duplicate, so the list is not sorted
        return false; // found an element that's not in ascending order
    }
    return true;
}