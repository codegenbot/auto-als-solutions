#include <vector>
#include <algorithm>

bool issame(int a, int b) {
    if(a == 0 || b == 0)
        return false;
    return (a % b == 0 || b % a == 0);
}

vector<float> get_positive(vector<float> l) {
    vector<float> result;
    for (float x : l) {
        if (x > 0) {
            result.push_back(x);
        }
    }
    return result;