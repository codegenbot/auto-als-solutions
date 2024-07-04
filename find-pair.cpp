#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int n, target;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    cin >> target;

    unordered_map<int, int> num_map;
    for (int i = 0; i < n; ++i) {
        int complement = target - nums[i];
        if (num_map.find(complement) != num_map.end()) {
            cout << complement << endl;
            cout << nums[i] << endl;
            return 0;
        }
        num_map[nums[i]] = i;
    }
    return 0;
}