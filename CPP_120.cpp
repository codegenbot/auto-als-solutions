#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

vector<int> maximum(vector<int> arr, int k) {
    priority_queue<int> pq;
    for (int i : arr) {
        pq.push(i);
        if (pq.size() > k) {
            pq.pop();
        }
    }
    vector<int> result;
    while (!pq.empty()) {
        result.push_back(pq.top());
        pq.pop();
    }
    return result;
}

int main() {
    // Check the output
    assert(issame(maximum({1, 2, 3, -23, 243, -400, 0}, 0) , {}));
    return 0;
}