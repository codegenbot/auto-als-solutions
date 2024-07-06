#include <algorithm>
#include <vector>
#include <bitset>

using namespace std;

vector<int> sort_array(vector<int> arr) {
    sort(arr.begin(), arr.end(), [](int a, int b) {
        bitset<32> bits_a(a);
        bitset<32> bits_b(b);
        if (bits_a.count() != bits_b.count())
            return bits_a.count() < bits_b.count();
        else
            return a < b;
    });
    return arr;
}