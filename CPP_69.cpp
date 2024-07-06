#include <vector>
using namespace std;

int search(vector<int> lst) {
    map<int, int> freq;
    for (auto x : lst) {
        if (freq.find(x) != freq.end()) {
            freq[x]++;
        } else {
            freq[x] = 1;
        }
    }
    for (auto p : freq) {
        if (p.second >= p.first) {
            return p.first;
        }
    }
    return -1;
}