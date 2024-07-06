int next_smallest(vector<int> lst){
    if(lst.size() < 2) return -1; // None is represented by -1
    vector<int> temp = lst;
    sort(temp.begin(),temp.end());
    for(int i=0;i<temp.size()-1;++i)
        if(temp[i]!=temp[i+1])
            return temp[i];
    return -1; // Return -1 as there is no 2nd smallest element
}