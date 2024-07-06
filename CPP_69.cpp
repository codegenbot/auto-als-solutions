#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<int> vec(vec.begin(), vec.end());
    assert(std::search(vec.begin(), vec.end(), vec.begin(), vec.end()) == vec.end());
    return 0;
}