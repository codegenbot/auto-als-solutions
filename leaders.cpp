#include <vector>
using namespace std;

vector<int> leaders(vector<int>& vec) {
    int rightmost = -1;
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i] >= rightmost) {
            rightmost = vec[i];
        }
    }

    vector<int> result;
    for (int i = vec.size() - 1; i >= 0; i--) {
        if (vec[i] >= rightmost) {
            result.push_back(vec[i]);
        }
    }

    return result;
}