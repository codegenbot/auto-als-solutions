#include <vector>
#include <boost/any.hpp>

bool issame(const vector<int>& a, const vector<int>& b) {
    return a.size() == b.size() && all_of(a.begin(), a.end(), [&](int x) { return count(b.begin(), b.end(), x) > 0; });
}

int main() {
    assert(issame(filter_integers({3, 'c', 3, 3, 'a', 'b'}), {3, 3, 3}));
    return 0;
}