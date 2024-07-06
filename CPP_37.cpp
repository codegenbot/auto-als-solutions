#include <algorithm>
using namespace std;

vector<float> sort_even(vector<float> l) {
    vector<float> evens, odds;
    for(int i = 0; i < l.size(); i++) {
        if(i % 2 == 0) evens.push_back(l[i]);
        else odds.push_back(l[i]);
    }
    sort(evens.begin(), evens.end());
    vector<float> result;
    for(auto x : odds) result.push_back(x);
    for(auto x : evens) result.push_back(x);
    return result;
}