#include <vector>
using namespace std;

int search(vector<int> lst) {
    int max = -1;
    for (auto x : lst) {
        if (x > 0 && x <= count(lst.begin(), lst.end(), x)) {
            max = x;
        }
    }
    return max;
}