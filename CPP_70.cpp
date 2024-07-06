```cpp
#include <vector>
#include <algorithm>

vector<int> strange_sort_vector(vector<int> lst) {
    vector<int> result;
    if (lst.empty()) return result;

    sort(lst.begin(), lst.end()); // Sort the list in ascending order

    while (!lst.empty()) {
        result.push_back(*lst.begin()); // Add the smallest element to the result
        lst.erase(lst.begin());
        if (!lst.empty())
            sort(lst.begin(), lst.end()); // Sort the remaining elements
    }

    return result;
}