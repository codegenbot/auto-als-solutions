#include <iostream>
#include <vector>
using namespace std;

// Function to generate integers within a range
vector<int> generate_integers(int start, int end) {
    vector<int> result;
    for (int i = start; i <= end; ++i) {
        result.push_back(i);
    }
    return result;
}

// Function to compare two integer vectors for sameness
bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

// Main function
int main_test() {
    assert(issame(generate_integers(17, 89), generate_integers(17, 89)));
    return 0;
}