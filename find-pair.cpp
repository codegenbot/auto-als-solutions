#include <vector>
using namespace std;

pair<int, int> findPair(vector<int>& vec, int target) {
    unordered_map<int, int> mp;
    for (int num : vec) {
        int complement = target - num;
        if (mp.find(complement) != mp.end()) {
            return {complement, num};
        }
        mp[num] = 1;
    }
    return {-1, -1}; // return empty pair when no pair is found
}

int main() {
    int n;
    cin >> n;
    vector<int> vec(n);
    for (auto& x : vec) cin >> x;
    int target;
    cin >> target;
    auto res = findPair(vec, target);
    if (res.first == -1) cout << "No pair found" << endl;
    else {
        cout << res.first << " ";
        cout << res.second << endl;
    }
    return 0;
}