bool is_sorted(vector<int> lst){
    for(int i=1; i<lst.size(); i++){
        if(lst[i-1] >= lst[i]) return false;
        bool duplicate = false;
        for(int j=i-1; j>=0 && !duplicate; j--){
            if(lst[j] == lst[i]){
                duplicate = true;
                break;
            }
        }
        if(!duplicate) return false;
    }
    return true;
}