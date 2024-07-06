```
int next_smallest(vector<int> lst){
    if(lst.empty()) return -1;  // Return None which is equivalent to -1 in this case
    sort(lst.begin(), lst.end());
    if (lst.size() < 2) return -1;
    return lst[1];
}