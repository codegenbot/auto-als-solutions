#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<int> vec = {3, 10, 10, 9, 2};
    assert(std::search(vec.begin(), vec.end(), &vec[0], &vec[0]) == vec.end());
    return 0;
}