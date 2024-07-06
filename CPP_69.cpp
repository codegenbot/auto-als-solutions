#include <algorithm>
#include <vector>
using namespace std;

int search(vector<int> vec) {
    int target = 10; // the number you want to find
    auto it = find(vec.begin(), vec.end(), target);
    if (it != vec.end()) {
        return distance(it, vec.end());
    }
    return -1;
}

int main() {
    vector<int> vec = {3, 10, 10, 9, 2};
    assert(search(vec) == -1); 
    return 0;
}