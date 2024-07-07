#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

vector<int> sort_array(vector<int> arr) {
    vector<int> result = arr;
    sort(result.begin(), result.end(), [](int a, int b) {
        bitset<32> bs_a(a);
        bitset<32> bs_b(b);
        return bs_a.count() == bs_b.count() ? a < b : bs_a.count() < bs_b.count();
    });
    return result;
}