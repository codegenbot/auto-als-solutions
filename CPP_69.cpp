#include <algorithm>
#include <vector>
#include <initializer_list>
using namespace std;

int main() {
    vector<int> vec = {3, 10, 10, 9, 2};
    assert(std::search(vec.begin(), vec.end(), vec.begin(), vec.end()) == vec.end());
    return 0;
}