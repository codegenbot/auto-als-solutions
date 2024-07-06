#include <vector>
using namespace std;

bool issame(vector<int> a, vector<int> b) {
    return a == b;
}

vector<int> sort_array(vector<int> array){
    int first = array.empty() ? 0 : array[0];
    int last = array.empty() ? 0 : array.back();
    if ((first + last) % 2 == 1)
        return vector<int>(array);
    else
        return vector<int>(array.rbegin(), array.rend());
}

int main() {
    assert(isame(sort_array({21, 14, 23, 11}) , {23, 21, 14, 11}));
    return 0;
}