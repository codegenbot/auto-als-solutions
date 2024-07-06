#include <vector>
#include <algorithm>

using namespace std;

vector<int> pluck(vector<int> arr) {
    vector<int> result = {};
    int minEvenValue = INT_MAX;
    bool found = false;

    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < minEvenValue) {
            minEvenValue = arr[i];
            result = {minEvenValue, i};
            found = true;
        }
    }

    return result;
}