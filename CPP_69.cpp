#include <vector>
using namespace std;

int search(vector<int> lst) {
    int max_freq = 0;
    for (int num : lst) {
        if (num > 0) {
            int freq = count(lst.begin(), lst.end(), num);
            if (freq >= num && freq > max_freq) {
                max_freq = freq;
            }
        }
    }
    return max_freq >= 1 ? max_freq : -1;
}