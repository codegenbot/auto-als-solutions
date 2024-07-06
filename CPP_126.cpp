bool is_sorted(vector<int> lst) {
    for(int i = 1; i < lst.size(); i++){
        if(lst[i-1] >= lst[i]){
            return false;
        }
    }
    auto last = unique(lst.begin(), lst.end());
    return last == lst.end();
}