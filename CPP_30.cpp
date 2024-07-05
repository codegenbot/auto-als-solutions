#include <initializer_list>
#include <vector>
using namespace std;

bool issame(vector<vector<float>>& a, vector<vector<float>>& b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i<a.size(); i++)
        if (abs(a[i][0] - b[i][0]) > 1e-9)
            return false;
    return true;
}

vector<float> get_positive(vector<float> l) {
    vector<float> result;
    for (float x : l) {
        if (x > 0)
            result.push_back(x);
    }
    return result;
}

int main_test() {
    return 0;
}