#include <algorithm>
#include<vector>
using namespace std;

vector<int> largest_smallest_integers(vector<int> lst) {
    pair<int,int> result = make_pair(0, 0);

    for (int num : lst) {
        if (num < 0) {
            result.first = max(result.first, num);
        }
        else if (num > 0) {
            result.second = min(result.second, num);
        }
    }

    return {result.first, result.second};
}