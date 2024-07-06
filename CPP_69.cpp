#include <vector>
#include <map>

using namespace std;

int search(vector<int> lst) {
    map<int, int> freq;
    for (int x : lst) {
        if (freq.find(x) == freq.end())
            freq[x] = 0;
        else if (++freq[x] >= 2)
            return x;
    }
    
    return -1;
}