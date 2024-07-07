#include <iostream>
#include <vector>
#include <queue>

using namespace std;

bool issame(vector<int> a,vector<int>b){
    if(a.size() != b.size())
        return false;
    for(int i=0; i<a.size();i++){
        if(a[i] != b[i])
            return false;
    }
    return true;
}

vector<int> maximum(vector<int> arr, int k) {
    priority_queue<int> pq;
    for (int i : arr) {
        pq.push(i);
    }
    vector<int> res;
    while (!pq.empty() && res.size() < k) {
        res.push_back(pq.top());
        pq.pop();
    }
    return res;
}

int main() {
    assert(issame(maximum({1, 2, 3, -23, 243, -400, 0}, 3), {0, 2, 243}));
    return 0;
}