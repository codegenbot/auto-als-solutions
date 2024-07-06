#include <vector>
#include <algorithm>

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

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

int main() {
    vector<int> result = strange_sort_vector({111111});
    assert(issame(result, vector<int>{111111}));
    return 0;
}