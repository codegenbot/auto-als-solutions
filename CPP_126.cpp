Here's the completed code:

bool is_sorted(vector<int> lst) {
    if (lst.size() <= 1) return true; // single element or empty vector
    bool sorted = true;
    for (int i = 1; i < lst.size(); ++i) {
        if (lst[i] <= lst[i-1]) { // not strictly increasing
            if (count(lst.begin(), lst.end(), lst[i]) > 1) return false; // duplicate found
            sorted = false;
            break;
        }
    }
    return sorted;
}