#include <vector>
#include <map>

using namespace std;

int search(vector<int> lst) {
    map<int, int> freq;
    for (int x : lst) {
        if (freq.find(x) == freq.end())
            freq[x] = 1;
        else
            freq[x]++;
    }
    
    for (pair<int, int> p : freq) {
        if (p.second >= p.first)
            return p.first;
    }
    
    return -1;
}