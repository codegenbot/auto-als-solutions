int next_smallest(vector<int> lst) {
    if (lst.empty()) return -1;  // or any other value that represents "None"
    
    vector<int> sorted = lst;
    sort(sorted.begin(), sorted.end());
    
    auto it = prev(end(sorted));
    if (distance(it, end(sorted)) == 1)
        return -1;  // or any other value that represents "None"
    
    return *it;
}