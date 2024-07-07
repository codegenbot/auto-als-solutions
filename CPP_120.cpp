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