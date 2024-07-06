int next_smallest(vector<int> lst){
    if(lst.size() < 2) return -1; // Return None
    vector<int> temp = lst;
    sort(temp.begin(), temp.end());
    for(int i = 0; i < temp.size(); i++){
        if(i == 0 || temp[i] != temp[i-1]){
            if(i == 1){
                return temp[i];
            }
        }
    }
    return -1; // Return None
}