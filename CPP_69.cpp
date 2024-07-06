#include <algorithm>
#include <vector>
using namespace std;

int main() {
    vector<int> vec = {3, 10, 10, 9, 2};
    assert(find(vec.begin(), vec.end(), 10) != vec.end()); 
    return 0;
}