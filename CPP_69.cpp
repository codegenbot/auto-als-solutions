// Your code should return the count of smallest number that has same frequency as any other number.

#include <iostream>
using namespace std;

int search(vector<int> lst) {
    map<int, int> freq;
    for (int num : lst) {
        if (freq.find(num) == freq.end()) {
            freq[num] = 1;
        } else {
            freq[num]++;
        }
    }
    int min_freq = INT_MAX;
    for (auto p : freq) {
        if (p.second < min_freq) {
            min_freq = p.second;
        }
    }
    for (auto p : freq) {
        if (p.second == min_freq && p.first > 0) {
            return p.first;
        }
    }
    return -1;
}

int main() {
    vector<int> lst = {3, 10, 10, 9, 2};
    cout << search(lst);
    return 0;
}