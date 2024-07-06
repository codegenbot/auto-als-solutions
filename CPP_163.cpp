#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

std::vector<int> generate_integers(int& a, int& b) {
    vector<int> result;
    for (int i = min(a, b); i <= max(a, b); i++) {
        if (i % 2 == 0) {
            result.push_back(i);
        }
    }
    return result;
}

bool issame(const vector<int>& a, const vector<int>&b){
    return (a==b);
}

int main_test() { 
    assert(issame(generate_integers(17,89), generate_integers(17,89)));
    return 0;
}