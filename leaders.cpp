#include <vector>
using namespace std;

vector<int> leaders(vector<int>& arr) {
    vector<int> leaders;
    int rightMost = arr.back();
    for (int i = arr.size() - 2; i >= 0; --i) {
        if (arr[i] >= rightMost) {
            rightMost = arr[i];
            leaders.push_back(rightMost);
        }
    }
    return leaders;
}