#include <vector>
#include <algorithm>

using namespace std;

vector<int> unique(vector<int> l) {
    vector<int> result(l.begin(), unique_element(l.begin(), l.end()));
    return result;
}

vector<int>::iterator unique_element(vector<int>::iterator start, vector<int>::iterator end) {
    sort(start, end);
    auto it = start;
    while (it != end) {
        auto next = it + 1;
        while (next != end && *next == *it) {
            ++next;
        }
        it = next;
    }
    return it;
}