#include <vector>
using namespace std;

vector<int> leaders(vector<int> v) {
    vector<int> res;
    int maxRight = v.back();
    for(int i=v.size()-2; i>=0; i--) {
        if(v[i] >= maxRight) {
            res.push_back(v[i]);
            maxRight = v[i];
        }
    }
    return res;