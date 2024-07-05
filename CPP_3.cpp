#include <vector>
#include <algorithm>
using namespace std;

bool below_zero(vector<int> operations) {
    return std::any_of(operations.begin(), operations.end(), [](int x) {return x < 0;});
}